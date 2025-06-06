# resetHandler

**Framework**: Core Haptics  
**Kind**: property

A block that the haptic engine calls after recovering from a haptic server error.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var resetHandler: CHHapticEngine.ResetHandler { get set }
```

#### Discussion

If the handler has to reset itself after a server failure, the system calls this block asynchronously. In this block, release all haptic pattern players and recreate them. The system preserves [`CHHapticPattern`](chhapticpattern.md) objects and [`CHHapticEngine`](chhapticengine.md) properties across restarts. Consider trying to restart the engine inside the reset block.

Callbacks to this block arrive on a non-main thread, so handle them in a thread-safe manner.

## See Also

- [CHHapticEngine.ResetHandler](chhapticengine/resethandler-swift.typealias.md)
  A typealias for the block that the haptic engine calls after being reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/resethandler-swift.property)*