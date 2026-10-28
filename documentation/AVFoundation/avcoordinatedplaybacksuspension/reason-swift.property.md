# reason

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The reason for the suspension.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var reason: AVCoordinatedPlaybackSuspension.Reason { get }
```

```objc
@property (nonatomic, readonly) AVCoordinatedPlaybackSuspensionReason reason;
```

## Discussion

The coordinator communicates the suspension reason to other participants.

## See Also

### Inspecting a suspension
- [var beginDate: Date](./begindate.md)
  The time the suspension begins.
- [AVCoordinatedPlaybackSuspension.Reason](./reason-swift.struct.md)
  Constants that identify playback suspension reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.property)*