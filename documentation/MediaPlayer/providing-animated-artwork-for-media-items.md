# Providing animated artwork for media items

**Framework**: Media Player

Display animated artwork for your app’s media in system views, such as the lock screen, by providing video assets through your now playing info.

#### Overview

If your app provides media with static artwork (such as music with associated album artwork), you can augment your media with additional expressive animated artwork that the system may display in place of the static artwork. Use animated artwork to highlight unique aspects of your content and provide a more immersive experience for people who use your app. To make your content more appealing, aim to provide animated artwork that functions as an extension of your static artwork, such as an animated variant of your existing static album artwork.

#### Provide Animated Artwork

Animated artwork consists of a video asset for the animated artwork itself and a static preview image which should ideally match the first frame of the video. The system displays the preview image while loading the video into the view, or under certain device conditions, including when:

- the device is in low-power mode
- the device is in low-data mode
- the device’s thermal level is too high
- a person turns on the Reduce Motion setting in Settings > Accessibility > Motion
- a person turns off the Auto-Play Animated Images setting in Settings > Accessibility > Motion

Provide animated artwork alongside existing media item metadata through [`MPNowPlayingInfoCenter`](mpnowplayinginfocenter.md). Use the key appropriate for the aspect ratio of your animated artwork within [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md):

```swift
MPNowPlayingInfoCenter.default().nowPlayingInfo = [
    // Existing media item metadata.
    MPMediaItemPropertyTitle: songTitle,
    MPMediaItemPropertyAlbumTitle: albumTitle,
    // ... other keys.

    // Animated artwork keys.
    MPNowPlayingInfoProperty1x1AnimatedArtwork: squareAnimatedArtwork,
    MPNowPlayingInfoProperty3x4AnimatedArtwork: tallAnimatedArtwork,
]
```

Provide animated artwork for either, neither, or both of these keys, depending on the available formats for your media. Depending on the current platform, the system only uses certain variants of animated artwork. Query [`supportedAnimatedArtworkKeys`](mpnowplayinginfocenter/supportedanimatedartworkkeys.md) to fetch the animated artwork keys that are relevant for the current platform. The system ignores any animated artwork you provide to [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md) for a key not in this collection.

```swift
let availableKeys = MPNowPlayingInfoCenter.supportedAnimatedArtworkKeys
let squareArtworkSupported = availableKeys.contains(MPNowPlayingInfoProperty1x1AnimatedArtwork)
let tallArtworkSupported = availableKeys.contains(MPNowPlayingInfoProperty3x4AnimatedArtwork)
```

#### Construct Animated Artwork

For each animated artwork variant you want to provide, include an [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) instance keyed by the relevant animated artwork key in the now playing info you set to [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md).  Each [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) describes the animated artwork content for a single variant. Initialize an instance with an `artworkID` (uniquely identifying the artwork for the associated variant), and request handlers for the preview image and video asset (`previewImageRequestHandler` and `videoAssetFileURLRequestHandler`, respectively).

The system uses the `artworkID` to detect changes in the provided animated artwork. When you need to change your animated artwork, provide a new [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) to [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md) with an updated `artworkID`. This prompts the system to re-request the preview image and video asset, if required. Aim to use the same `artworkID` between media items if the animated artwork doesn’t change; for example, the album artwork for songs within an album is constant.

#### Return Animated Artwork Assets

When the system requires a preview image, it uses the `previewImageRequestHandler` for the currently-provided [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) (for the required animated artwork variant). It passes the dimensions of the requested image to this handler; however, you can return an image of any size as long as the aspect ratio is appropriate for the associated animated artwork key. You can use the requested size if you require this information in order to provide the resulting preview image.

> ❗ **Important**:  If you return a preview image with an incorrect aspect ratio, like a non-square image from an [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) associated with the [`MPNowPlayingInfoProperty1x1AnimatedArtwork`](mpnowplayinginfoproperty1x1animatedartwork.md) key, the system will ignore your animated artwork and display your static artwork.

Similarly, when the system requires the video asset, it uses the `videoAssetFileURLRequestHandler` for the relevant [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md). The same considerations around the requested pixel dimensions passed to this handler apply: you can provide a video of any size as long as it matches the aspect ratio of the associated animated artwork key. As part of your handler, return a local file URL for the artwork video. The system doesn’t support remote or streaming URLs.

Provide preview images from your `previewImageRequestHandler` quickly, and ideally synchronously. If you provide an [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) as part of your now playing info but fail to provide a preview image in a timely manner when requested, the system may fallback to displaying the static artwork while it waits for the preview image to become available. Conversely, you can require additional time to return your video assets from your `videoAssetFileURLRequestHandler`. For example, you can download the required video over the network, when requested, before returning a local file URL to the resulting on-disk asset. The system displays the preview image during this time. Avoid excessive latency when you return this local file URL, as the system may timeout the request after 30 seconds.

```swift
// Call when `currentSong` changes.
func updateInfoCenter() {
    let currentSong = self.currentSong

    let squareAnimatedArtwork = MPMediaItemAnimatedArtwork(
        artworkID: currentSong.artworkID,
        previewImageRequestHandler: { _ in
            // When possible, have the preview image available synchronously when building the
            // `MPMediaItemAnimatedArtwork`.
            currentSong.squareAnimatedArtwork.previewFrame
        },
        videoAssetFileURLRequestHandler: { _ in
            do {
                // Retrieve the video asset on demand, saving it locally and providing a local
                // file URL.
                let assetFileURL = Self.videoAssetStorage.makeAssetFileURL()
                try await currentSong.squareAnimatedArtwork.fetchVideo(destination: assetFileURL)
                return assetFileURL
            } catch {
                // If you’re unable to provide the video asset, return `nil`.
                return nil
            }
        }
    )

    MPNowPlayingInfoCenter.default().nowPlayingInfo = [
        MPNowPlayingInfoProperty1x1AnimatedArtwork: squareAnimatedArtwork,
        // ... other keys.
    ]
}
```

Ensure any local file URLs you return from a `videoAssetFileURLRequestHandler` remain valid for as long as the associated [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) is part of your now playing info. You can invalidate these URLs — for example, when you need to delete the associated asset — when you replace (or remove) the [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) in your now playing info. If you later provide an [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) with an `artworkID` that’s identical to one you provided previously, you don’t need to provide the same assets, as the system re-requests them.

#### Follow Asset Recommendations

Ensure the aspect ratio of any preview images or video assets you provide matches the aspect ratio indicated by the animated artwork key you associate the [`MPMediaItemAnimatedArtwork`](mpmediaitemanimatedartwork.md) with. Avoid high frame rate video (greater than 60 fps), as the system may not display your animated artwork. The system doesn’t impose a technical limitation on the file size of the video assets you provide, and it supports any local asset playable by an `AVPlayerLayer`.

For videos, the system prefers a short (less than 30 second) clip that loops seamlessly. Avoid a noticeable jump or fade effect when the video repeats. Make your videos complementary to any existing static artwork you provide, and avoid providing video content unrelated to the playing media item.

The system only requests the preview image and video asset when someone is viewing the animated artwork. Avoid performing expensive network requests for video assets in advance, as the system may ultimately not request the asset. The system doesn’t cache assets between different `artworkID`s. To prevent unnecessary downloads if you want to display the same artwork again, consider caching your video assets locally.

## See Also

- [class MPMediaItem](mpmediaitem.md)
  A collection of properties that represents a single item in the media library.
- [class MPMediaItemArtwork](mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaItemAnimatedArtwork](mpmediaitemanimatedartwork.md)
  An animated image, such as an animated music album cover art, for a media item.
- [class MPMediaItemCollection](mpmediaitemcollection.md)
  A sorted set of media items from the media library.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/providing-animated-artwork-for-media-items)*