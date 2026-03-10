# init(preferredPresentation:playbackAction:elapsedTime:duration:)

**Framework**: CarPlay  
**Kind**: init

Initialize a description of the playable media content that is represented by template items.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
init(preferredPresentation: CPPlaybackConfiguration.Presentation, playbackAction: CPPlaybackConfiguration.Action, elapsedTime: CMTime, duration: CMTime)
```

#### Discussion

> **Note**: Video presentation may be unsupported for this session  (see `-[CPSessionConfiguration videoPlaybackSupported]`) or may be unavailable due to playback policy.

## Parameters

- `preferredPresentation`: The preferred style of media presentation shown after selecting the item.
- `playbackAction`: The playback action to perform on this item, such as play, pause, or replay.
- `elapsedTime`: The elapsed playback time as a CMTime value.
- `duration`: The total duration of the media content as a CMTime value. Provide 0 if the duration of the content is unknown or unavailable, for example in live-streaming content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/init(preferredpresentation:playbackaction:elapsedtime:duration:))*