# endTime

**Framework**: AVFoundation  
**Kind**: property

The presentation time of the first frame following the end of a reaction effect.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var endTime: CMTime { get }
```

#### Discussion

The value is [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid) while the effect is in progress, but changes to a valid time when the reaction effect completes and the system removes it from the list of [`reactionEffectsInProgress`](avcapturedevice/reactioneffectsinprogress.md).

## See Also

- [var reactionType: AVCaptureReactionType](avcapturereactioneffectstate/reactiontype.md)
  The type of reaction.
- [struct AVCaptureReactionType](avcapturereactiontype.md)
  Constants that indicate the type of reaction that an effect can perform.
- [var startTime: CMTime](avcapturereactioneffectstate/starttime.md)
  The presentation time of the first frame where the system renders the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate/endtime)*