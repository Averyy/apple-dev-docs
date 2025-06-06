# GCControllerTouchpad.TouchState

**Framework**: Game Controller  
**Kind**: enum

The possible states of the user’s touch.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum TouchState
```

## Topics

### States
- [GCControllerTouchpad.TouchState.up](gccontrollertouchpad/touchstate-swift.enum/up.md)
  The user stops or isn’t touching the surface.
- [GCControllerTouchpad.TouchState.down](gccontrollertouchpad/touchstate-swift.enum/down.md)
  The user starts touching the surface.
- [GCControllerTouchpad.TouchState.moving](gccontrollertouchpad/touchstate-swift.enum/moving.md)
  The user continues touching the surface.
### Initializers
- [init?(rawValue: Int)](gccontrollertouchpad/touchstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var touchState: GCControllerTouchpad.TouchState](gccontrollertouchpad/touchstate-swift.property.md)
  The state of the user’s touch on the surface of the touchpad.
- [var reportsAbsoluteTouchSurfaceValues: Bool](gccontrollertouchpad/reportsabsolutetouchsurfacevalues.md)
  A Boolean value that determines whether the touch values are absolute or relative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad/touchstate-swift.enum)*