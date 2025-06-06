# CHHapticEngine.StoppedHandler

**Framework**: Corehaptics  
**Kind**: typealias

A typealias for the block that the haptic engine calls after it stops due to an external cause.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias StoppedHandler = (CHHapticEngine.StoppedReason) -> Void
```

#### Discussion

The system calls the stopped handler for when it’s stopped by an external event like an audio session interruption or an auto-shutdown.

> **Note**:  The stopped handler isn’t called if you explicitly stop the engine by calling the [`stop(completionHandler:)`](chhapticengine/stop(completionhandler:).md) method.

## See Also

- [var stoppedHandler: CHHapticEngine.StoppedHandler](chhapticengine/stoppedhandler-swift.property.md)
  A closure the haptic engine calls when it stops due to external causes.
- [CHHapticEngine.StoppedReason](chhapticengine/stoppedreason.md)
  The enumeration of reasons the haptic engine stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedhandler-swift.typealias)*