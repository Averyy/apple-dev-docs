# CHHapticEngine.ResetHandler

**Framework**: Core Haptics  
**Kind**: typealias  
**Role**: Type Alias

A typealias for the block that the haptic engine calls after being reset.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias ResetHandler = () -> Void
```

```c
typedef void (^)(void) CHHapticEngineResetHandler;
```

## See Also

### Handling Haptic Engine Resets
- [var resetHandler: CHHapticEngine.ResetHandler](./resethandler-swift.property.md)
  A block that the haptic engine calls after recovering from a haptic server error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/resethandler-swift.typealias)*