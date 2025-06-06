# stoppedHandler

**Framework**: Core Haptics  
**Kind**: property

A closure the haptic engine calls when it stops due to external causes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var stoppedHandler: CHHapticEngine.StoppedHandler { get set }
```

## Mentions

- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)

#### Discussion

External causes that can cause the system to call this closure include audio session interruptions, app suspensions, or system errors. Calling [`stop(completionHandler:)`](chhapticengine/stop(completionhandler:).md) doesn’t invoke this callback.

Callbacks to this closure don’t occur on the main thread, so handle them in a thread-safe manner.

## See Also

- [CHHapticEngine.StoppedHandler](chhapticengine/stoppedhandler-swift.typealias.md)
  A typealias for the block that the haptic engine calls after it stops due to an external cause.
- [CHHapticEngine.StoppedReason](chhapticengine/stoppedreason.md)
  The enumeration of reasons the haptic engine stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/stoppedhandler-swift.property)*