# init(preferredPresentation:playbackAction:elapsedTime:duration:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a playback configuration object with the specified presentation style, playback action, and media details.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(preferredPresentation: CPPlaybackConfiguration.Presentation, playbackAction: CPPlaybackConfiguration.Action, elapsedTime: CMTime, duration: CMTime)
```

```objc
- (instancetype) initWithPreferredPresentation:(CPPlaybackPresentation) preferredPresentation playbackAction:(CPPlaybackAction) playbackAction elapsedTime:(CMTime) elapsedTime duration:(CMTime) duration;
```

## Return Value

An initialized configuration object.

## Parameters

- `preferredPresentation`: The preferred way to present the media when someone selects it. The system can configure a playback interface automatically, or you can present the interface yourself.
- `playbackAction`: The action to take when someone selects the item.
- `elapsedTime`: The elapsed playback time for the media. This parameter indicates at which point to start playing the media.
- `duration`: The duration of the media content in seconds. Specify `0` if the duration is unknown or unavailable. For example, you might specify `0` for live-streaming content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/init(preferredpresentation:playbackaction:elapsedtime:duration:))*