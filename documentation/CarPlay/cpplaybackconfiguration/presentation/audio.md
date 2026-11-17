# CPPlaybackConfiguration.Presentation.audio

**Framework**: CarPlay  
**Kind**: case  
**Role**: Case

An option to display the Now Playing interface automatically and configure it with the item.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
case audio
```

```c
CPPlaybackPresentationAudio
```

## Discussion

When someone selects the item, the system automatically displays your app’s shared [`CPNowPlayingTemplate`](../../cpnowplayingtemplate.md) object. You don’t need to push the [`CPNowPlayingTemplate`](../../cpnowplayingtemplate.md) object programmatically from your app when someone selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/presentation/audio)*