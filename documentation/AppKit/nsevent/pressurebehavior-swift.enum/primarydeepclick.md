# NSEvent.PressureBehavior.primaryDeepClick

**Framework**: AppKit  
**Kind**: case

A pressure gesture’s behavior begins on left mouse-down events. Two stages are supported, and a stage transition animation may occur when moving between stages—from stage 1 to stage 0, stage 1 to stage 2, stage 2 to stage 1, and stage 2 to stage 0. With this behavior type, stage 2 becomes disabled once dragging occurs. When this behavior is configured, actuations occur during the mouse-down and mouse-up events, as well as when force click is activated and released when entering or exiting stage 2. This configuration is ideal for responding to force clicks. Note that the pressure gesture operates on a separate event stream from the mouse events.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
case primaryDeepClick
```

## See Also

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
- [NSEvent.PressureBehavior.primaryDeepDrag](nsevent/pressurebehavior-swift.enum/primarydeepdrag.md)
  A pressure gesture’s behavior begins on left mouse-down events. Two stages are supported, and a stage transition animation may occur when moving between stages—from stage 1 to stage 0, stage 1 to stage 2, stage 2 to stage 1, or stage 2 to stage 0. Actuations occur during the mouse-down and mouse-up events, as well as during the transitions up and down between stage 1 and stage 2, when this behavior is configured. This configuration is ideal for responding to force clicks during drag operations. Note that the pressure gesture operates on a separate event stream from the mouse events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pressurebehavior-swift.enum/primarydeepclick)*