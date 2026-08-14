# isAutoShutdownEnabled

**Framework**: Core Haptics  
**Kind**: property

A Boolean value that indicates whether the haptic engine starts and stops automatically on request from one of its pattern players, or when idle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isAutoShutdownEnabled: Bool { get set }
```

#### Discussion

If you manually manage the engine’s life cycle, save power by stopping the engine when it’s not in use. You can enable the engine to automatically manage this behavior by setting the value to [`true`](https://developer.apple.com/documentation/swift/true). When this property is enabled, the engine shuts down after approximately two minutes of inactivity.

Delegating this responsibility to the framework makes the engine more manageable, but you no longer have fine-grained control of its life cycle.

The default value is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/isautoshutdownenabled)*