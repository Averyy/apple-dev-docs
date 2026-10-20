# reactionType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) AVCaptureReactionType reactionType;
```

#### Discussion

There may be multiple reactions of the same type at a given time. Some may come from calls to [`performEffect(for:)`](../avcapturedevice/performeffect%28for%29.md) and others from gesture detection.

## See Also

### Configuring the effect state
- [struct AVCaptureReactionType](../avcapturereactiontype.md)
  Constants that indicate the type of reaction that an effect can perform.
- [var startTime: CMTime](./starttime.md)
  The presentation time of the first frame where the system renders the effect.
- [var endTime: CMTime](./endtime.md)
  The presentation time of the first frame following the end of a reaction effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate/reactiontype)*