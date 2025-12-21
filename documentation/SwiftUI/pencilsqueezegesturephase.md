# PencilSqueezeGesturePhase

**Framework**: SwiftUI  
**Kind**: enum

Describes the phase and value of an Apple Pencil squeeze gesture.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- visionOS 26.2+

## Declaration

```swift
@frozen
enum PencilSqueezeGesturePhase
```

#### Overview

When you use the [`onPencilSqueeze(perform:)`](view/onpencilsqueeze(perform:).md) view modifier, you can handle the Apple Pencil squeeze gesture’s phase in the `action` closure.

## Topics

### Enumeration Cases
- [case active(PencilSqueezeGestureValue)](pencilsqueezegesturephase/active(_:).md)
  The user started squeezing their Apple Pencil.
- [case ended(PencilSqueezeGestureValue)](pencilsqueezegesturephase/ended(_:).md)
  The user successfully completed a squeeze gesture.
- [PencilSqueezeGesturePhase.failed](pencilsqueezegesturephase/failed.md)
  The user started squeezing their Apple Pencil but failed to successfully complete the gesture.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](view/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](view/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [var preferredPencilDoubleTapAction: PencilPreferredAction](environmentvalues/preferredpencildoubletapaction.md)
  The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [var preferredPencilSqueezeAction: PencilPreferredAction](environmentvalues/preferredpencilsqueezeaction.md)
  The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [struct PencilPreferredAction](pencilpreferredaction.md)
  An action that the user prefers to perform after double-tapping their Apple Pencil.
- [struct PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md)
  Describes the value of an Apple Pencil double-tap gesture.
- [struct PencilSqueezeGestureValue](pencilsqueezegesturevalue.md)
  Describes the value of an Apple Pencil squeeze gesture.
- [struct PencilHoverPose](pencilhoverpose.md)
  A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilsqueezegesturephase)*