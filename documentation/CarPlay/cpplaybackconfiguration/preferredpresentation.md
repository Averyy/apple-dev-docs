# preferredPresentation

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The preferred presentation behavior when someone selects the media item.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var preferredPresentation: CPPlaybackConfiguration.Presentation { get }
```

```objc
@property (nonatomic, assign, readonly) CPPlaybackPresentation preferredPresentation;
```

## Discussion

When someone selects a media item, this property tells the system whether to update the app’s interface automatically to reflect the selection. For example, when someone selects an audio file, the system can display the app’s shared [`CPNowPlayingTemplate`](../cpnowplayingtemplate.md) interface automatically. If the value of this property is [`CPPlaybackConfiguration.Presentation.none`](./presentation/none.md), the system doesn’t provide any automatic behavior and your app is responsible for updating its interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/preferredpresentation)*