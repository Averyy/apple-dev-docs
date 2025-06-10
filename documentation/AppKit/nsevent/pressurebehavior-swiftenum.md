# NSEvent.PressureBehavior

**Framework**: AppKit  
**Kind**: enum

These constants describe the behavior and progression of a pressure gesture.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
enum PressureBehavior
```

#### Overview

These constants describe the behavior and progression of a pressure gesture. They allow you to configure how pressure from a pressure-sensitive device, such as the Force Touch trackpad, is interpreted by the system. For example, a drawing or painting app may adjust the behavior of pressure events to focus on variable pressure and prevent force clicks from occurring.

In most cases, a pressure gesture’s behavior goes into effect when the gesture event’s [`stage`](nsevent/stage.md) property reaches a value of `1` and remains in effect until the gesture event’s [`stage`](nsevent/stage.md) property reaches a value of `0`. This behavior corresponds to the behavior of simultaneously generated mouse-up and mouse-down events.

## Topics

### Constants
- [NSEvent.PressureBehavior.unknown](nsevent/pressurebehavior-swift.enum/unknown.md)
  A pressure gesture’s behavior is not known, perhaps because the input device does not support pressure gestures.
- [NSEvent.PressureBehavior.primaryDefault](nsevent/pressurebehavior-swift.enum/primarydefault.md)
  This is the default behavior when a pressure gesture’s behavior has not been explicitly configured. In OS X 10.10.3, this behavior defaults to the behavior of `NSPressureBehaviorPrimaryDeepClick`.
- [NSEvent.PressureBehavior.primaryClick](nsevent/pressurebehavior-swift.enum/primaryclick.md)
  A pressure gesture’s behavior begins on left mouse-down events. A maximum of one stage is supported, and a stage transition animation occurs when moving from stage 1 to stage 0. Actuations (haptic feedback the user feels) occur during mouse-down and mouse-up events when this behavior is configured. Note that the pressure gesture operates on a separate event stream from the mouse events.
- [NSEvent.PressureBehavior.primaryGeneric](nsevent/pressurebehavior-swift.enum/primarygeneric.md)
  A pressure gesture’s behavior begins on left mouse-down events. A maximum of one stage is supported, and a stage transition animation occurs when moving from stage 1 to stage 0. Actuations occur during the mouse-down and mouse-up events when this behavior is configured. This configuration is ideal for drawing, painting, and general use. Variable pressure occurs throughout the course of the gesture. Note that the pressure gesture operates on a separate event stream from the mouse events.
- [NSEvent.PressureBehavior.primaryAccelerator](nsevent/pressurebehavior-swift.enum/primaryaccelerator.md)
  A pressure gesture’s behavior begins on left mouse-down events. A maximum of one stage is supported, and a stage transition animation occurs when moving from stage 1 to stage 0. Actuations occur during the mouse-down and mouse-up events when this behavior is configured. This configuration uses specific pressure mappings that are ideal for controlling speed as variable pressure occurs between the mouse-down and mouse-up events. The [`NSAcceleratorButton`](nsacceleratorbutton.md) class uses this behavior. Note that the pressure gesture operates on a separate event stream from the mouse events.
- [NSEvent.PressureBehavior.primaryDeepClick](nsevent/pressurebehavior-swift.enum/primarydeepclick.md)
  A pressure gesture’s behavior begins on left mouse-down events. Two stages are supported, and a stage transition animation may occur when moving between stages—from stage 1 to stage 0, stage 1 to stage 2, stage 2 to stage 1, and stage 2 to stage 0. With this behavior type, stage 2 becomes disabled once dragging occurs. When this behavior is configured, actuations occur during the mouse-down and mouse-up events, as well as when force click is activated and released when entering or exiting stage 2. This configuration is ideal for responding to force clicks. Note that the pressure gesture operates on a separate event stream from the mouse events.
- [NSEvent.PressureBehavior.primaryDeepDrag](nsevent/pressurebehavior-swift.enum/primarydeepdrag.md)
  A pressure gesture’s behavior begins on left mouse-down events. Two stages are supported, and a stage transition animation may occur when moving between stages—from stage 1 to stage 0, stage 1 to stage 2, stage 2 to stage 1, or stage 2 to stage 0. Actuations occur during the mouse-down and mouse-up events, as well as during the transitions up and down between stage 1 and stage 2, when this behavior is configured. This configuration is ideal for responding to force clicks during drag operations. Note that the pressure gesture operates on a separate event stream from the mouse events.
### Initializers
- [init?(rawValue: Int)](nsevent/pressurebehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var pressure: Float](nsevent/pressure.md)
  A normalized value that indicates the degree of pressure applied to an appropriate input device.
- [var stage: Int](nsevent/stage.md)
  A value that indicates the stage of a pressure gesture event.
- [var stageTransition: CGFloat](nsevent/stagetransition.md)
  The transition value for the stage of a pressure gesture event.
- [var pressureBehavior: NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.property.md)
  The behavior and progression for a pressure event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pressurebehavior-swift.enum)*