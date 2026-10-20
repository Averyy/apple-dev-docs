# Implementing trimming in a macOS player

**Framework**: AVKit  
**Role**: Article

Provide a QuickTime media-trimming experience in your macOS app.

#### Overview

You use [`AVPlayerView`](./avplayerview.md) to provide a playback experience like that of QuickTime Player in macOS. However, `AVPlayerView` not only provides the QuickTime playback interface, but it also provides the QuickTime media-trimming experience.

![Single image with multiple video frames selected and Trim button in an enabled state.](https://developer.apple.com/tutorials/images/com.apple.avkit/media-2948756@2x.png)

#### Verify that trimming is allowed

Before attempting to put the player into trimming mode, verify that trimming is allowed by querying the player view’s [`canBeginTrimming`](./avplayerview/canbegintrimming.md) property. This property returns `false` if you’re playing an asset delivered over HTTP Live Streaming or if the asset is content protected. If you’re presenting a menu item to initiate trimming, a good place to perform this check is in the [`validateUserInterfaceItem(_:)`](../AppKit/nsdocument/validateuserinterfaceitem%28_%29.md) method of [`NSDocument`](../AppKit/nsdocument.md), so that the menu item can automatically be disabled if trimming is disallowed.

```swift
override func validateUserInterfaceItem(_ item: NSValidatedUserInterfaceItem) -> Bool {
    if item.action == #selector(beginTrimming) {
        return playerView.canBeginTrimming
    }
    return super.validateUserInterfaceItem(item)
}
```

#### Enter trimming mode

After you’ve determined that the media supports trimming, you call the [`beginTrimming(completionHandler:)`](./avplayerview/begintrimming%28completionhandler%29.md). This method takes a completion block that you use to determine whether the user completed the trim or canceled the operation.

```swift
@IBAction func beginTrimming(_ sender: AnyObject) {
    playerView.beginTrimming { result in
        if result == .okButton {
            // user selected Trim button (AVPlayerViewTrimResult.okButton)...
        } else {
            // user selected Cancel button (AVPlayerViewTrimResult.cancelButton)...
        }
    }
}
```

#### Transcode the trimmed asset

Because [`AVAsset`](../AVFoundation/avasset.md) is an immutable object, you may be wondering how its duration is changed when you click the Trim button. Trimming relies on a feature of [`AVPlayerItem`](../AVFoundation/avplayeritem.md) to adjust the presented time range. `AVPlayerItem` provides the [`reversePlaybackEndTime`](../AVFoundation/avplayeritem/reverseplaybackendtime.md) and [`forwardPlaybackEndTime`](../AVFoundation/avplayeritem/forwardplaybackendtime.md) properties that set the in and out points for a media item. It doesn’t change the underlying asset, but essentially changes your effective view of it. To save the results of the user’s trim operation, you export a new copy of the asset, trimming it to the specified times. The simplest way to do this is to use [`AVAssetExportSession`](../AVFoundation/avassetexportsession.md), which provides a simple and performant way for you to transcode the media of an asset. You create a new export session, passing it the asset to export along with a transcoding preset to use.

```swift
// Transcoding preset
let preset = AVAssetExportPresetAppleM4V720pHD
let exportSession = AVAssetExportSession(asset: playerItem.asset, presetName: preset)!
exportSession.outputFileType = AVFileTypeAppleM4V
exportSession.outputURL = // Output URL
```

This example uses a preset to export the media as a 720p, M4V file, but `AVAssetExportSession` supports a wide variety of export presets. To find out what export session presets are supported for the current asset, you can use the session’s [`exportPresets(compatibleWith:)`](../AVFoundation/avassetexportsession/exportpresets%28compatiblewith%29.md) class method, passing it the asset you want to export. This method returns an array of valid presets that you can use in your export.

#### Select the trimmed asset

To export only the content the user trimmed, you use the current player item’s reverse and forward end-time values to define a [`CMTimeRange`](../CoreMedia/cmtimerange.md) to set on the export session.

```swift
// Create CMTimeRange with the trim in/out point times
let startTime = self.playerItem.reversePlaybackEndTime
let endTime = self.playerItem.forwardPlaybackEndTime
let timeRange = CMTimeRangeFromTimeToTime(startTime, endTime)
exportSession.timeRange = timeRange
```

#### Export the trimmed asset

To perform the actual export operation, you call its [`exportAsynchronously(completionHandler:)`](../AVFoundation/avassetexportsession/exportasynchronously%28completionhandler%29.md) method. Check the status of the export session in the completion handler and handle completion and failure cases.

```swift
exportSession.exportAsynchronously {
    switch exportSession.status {
    case .completed:
        // Export Complete
    case .failed:
        // failed
    default:
        // handle others
    }
}
```

## See Also

### Media trimming and export
- [Trimming and exporting media in visionOS](./trimming-and-exporting-media-in-visionos.md)
  Display standard controls in your app to edit the timeline of the currently playing media.
- [enum AVPlayerViewTrimResult](./avplayerviewtrimresult.md)
  Constants that specify an action a user takes when trimming media in a player view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/implementing-trimming-in-a-macos-player)*