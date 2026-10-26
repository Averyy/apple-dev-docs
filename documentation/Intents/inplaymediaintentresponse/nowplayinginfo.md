# nowPlayingInfo

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The now-playing information, such as title and artwork, for the media.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var nowPlayingInfo: [String : Any]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDictionary<NSString *,id> * nowPlayingInfo;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDictionary<NSString *,id> * nowPlayingInfo;
```

#### Discussion

In your [`confirm(intent:completion:)`](../inplaymediaintenthandling/confirm%28intent,completion%29.md) response, provide now-playing information for the media so Siri can display it to the user at the appropriate time, such as after they connect headphones to their iPhone.

To create the now-playing information dictionary, use the media item property keys from the Media Player framework (see [General media item property keys](../../MediaPlayer/general-media-item-property-keys.md) for the list of keys). To include artwork in the dictionary, use [`INImage`](../inimage.md) instead of [`UIImage`](../../UIKit/uiimage.md) to create the image object. Media intent shortcuts don’t support [`UIImage`](../../UIKit/uiimage.md) objects in this dictionary.

The listing below creates a now-playing information dictionary.

```swift
public static func nowPlayingInfo(for episode: PodcastEpisode, in container: LibraryItemContainer, forShortcut: Bool = false) -> [String: Any] {
    var nowPlayingInfo: [String: Any] = [MPMediaItemPropertyTitle: episode.title,
                                         MPMediaItemPropertyMediaType: MPMediaType.podcast.rawValue,
                                         MPMediaItemPropertyPodcastTitle: container.title,
                                         MPMediaItemPropertyPlaybackDuration: NSNumber(value: audioFileDuration)]

    if forShortcut {
        nowPlayingInfo[MPMediaItemPropertyArtwork] = INImage(named: container.artworkName)
    } else {
        if let image = UIImage(named: container.artworkName) {
            let artwork = MPMediaItemArtwork(boundsSize: CGSize(width: 60, height: 60)) { (_) -> UIImage in
                return image
            }
            
            nowPlayingInfo[MPMediaItemPropertyArtwork] = artwork
        }
    }
    
    return nowPlayingInfo
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponse/nowplayinginfo)*