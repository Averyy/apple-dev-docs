# CPPlaybackConfiguration.Presentation.video

**Framework**: CarPlay  
**Kind**: case  
**Role**: Case

An option to display the system video player automatically if it’s available and supported.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
case video
```

```c
CPPlaybackPresentationVideo
```

## Discussion

If video playback isn’t available, the system displays your app’s shared [`CPNowPlayingTemplate`](../../cpnowplayingtemplate.md) instead. You don’t need to push the [`CPNowPlayingTemplate`](../../cpnowplayingtemplate.md) object programmatically from your app in response to the item’s selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/presentation/video)*