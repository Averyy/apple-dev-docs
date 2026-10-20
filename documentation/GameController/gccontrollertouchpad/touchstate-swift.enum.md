# GCControllerTouchpad.TouchState

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GCTouchState : NSInteger;
```

## Topics

### States
- [GCControllerTouchpad.TouchState.up](./touchstate-swift.enum/up.md)
  The user stops or isn’t touching the surface.
- [GCControllerTouchpad.TouchState.down](./touchstate-swift.enum/down.md)
  The user starts touching the surface.
- [GCControllerTouchpad.TouchState.moving](./touchstate-swift.enum/moving.md)
  The user continues touching the surface.
### Initializers
- [init?(rawValue: Int)](./touchstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the input values
- [var touchState: GCControllerTouchpad.TouchState](./touchstate-swift.property.md)
  The state of the user’s touch on the surface of the touchpad.
- [var reportsAbsoluteTouchSurfaceValues: Bool](./reportsabsolutetouchsurfacevalues.md)
  A Boolean value that determines whether the touch values are absolute or relative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad/touchstate-swift.enum)*