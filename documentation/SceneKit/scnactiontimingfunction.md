# SCNActionTimingFunction

**Framework**: SceneKit  
**Kind**: typealias

The signature for a block that manages animation timing, used by the [`timingFunction`](scnaction/timingfunction.md) property.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias SCNActionTimingFunction = (Float) -> Float
```

#### Discussion

The block takes a single parameter:

Your block must return a floating-point value between `0.0` and `1.0`, where `0.0` represents the starting state of the action’s animation and `1.0` represents the end state.

## See Also

- [enum SCNActionTimingMode](scnactiontimingmode.md)
  Constants affecting the animation curve of an action, used by the [`timingMode`](scnaction/timingmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnactiontimingfunction)*