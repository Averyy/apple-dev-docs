# reactionType

**Framework**: AVFoundation  
**Kind**: property

The type of reaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var reactionType: AVCaptureReactionType { get }
```

#### Discussion

There may be multiple reactions of the same type at a given time. Some may come from calls to [`performEffect(for:)`](avcapturedevice/performeffect(for:).md) and others from gesture detection.

## See Also

- [struct AVCaptureReactionType](avcapturereactiontype.md)
  Constants that indicate the type of reaction that an effect can perform.
- [var startTime: CMTime](avcapturereactioneffectstate/starttime.md)
  The presentation time of the first frame where the system renders the effect.
- [var endTime: CMTime](avcapturereactioneffectstate/endtime.md)
  The presentation time of the first frame following the end of a reaction effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate/reactiontype)*