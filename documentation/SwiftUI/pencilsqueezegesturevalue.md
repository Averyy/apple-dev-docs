# PencilSqueezeGestureValue

**Framework**: SwiftUI  
**Kind**: struct

Describes the value of an Apple Pencil squeeze gesture.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+

## Declaration

```swift
struct PencilSqueezeGestureValue
```

## Topics

### Instance Properties
- [let hoverPose: PencilHoverPose?](pencilsqueezegesturevalue/hoverpose.md)
  The location and distance of an Apple Pencil hovering in the area above the view’s bounds when the squeeze gesture occurred.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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
- [enum PencilSqueezeGesturePhase](pencilsqueezegesturephase.md)
  Describes the phase and value of an Apple Pencil squeeze gesture.
- [struct PencilHoverPose](pencilhoverpose.md)
  A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pencilsqueezegesturevalue)*