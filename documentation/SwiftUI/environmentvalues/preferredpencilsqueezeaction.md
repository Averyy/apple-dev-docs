# preferredPencilSqueezeAction

**Framework**: SwiftUI  
**Kind**: property

The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+

## Declaration

```swift
var preferredPencilSqueezeAction: PencilPreferredAction { get }
```

#### Discussion

You can read this value by creating a property with the [`Environment`](environment.md) property wrapper and using it inside the action closure of the [`onPencilSqueeze(perform:)`](view/onpencilsqueeze(perform:).md) view modifier as an indication of what to do when the user squeezes their Apple Pencil:

```swift
@Environment(\.preferredPencilSqueezeAction) private var preferredAction

var body: some View {
    MyDrawingCanvas()
        .onPencilSqueeze { phase in
            switch (phase, preferredAction) {
                ...
            }
        }
}
```

In macOS, this value cannot be changed by users and is always set to [`showContextualPalette`](pencilpreferredaction/showcontextualpalette.md).

## See Also

- [func onPencilDoubleTap(perform: (PencilDoubleTapGestureValue) -> Void) -> some View](view/onpencildoubletap(perform:).md)
  Adds an action to perform after the user double-taps their Apple Pencil.
- [func onPencilSqueeze(perform: (PencilSqueezeGesturePhase) -> Void) -> some View](view/onpencilsqueeze(perform:).md)
  Adds an action to perform when the user squeezes their Apple Pencil.
- [var preferredPencilDoubleTapAction: PencilPreferredAction](environmentvalues/preferredpencildoubletapaction.md)
  The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [struct PencilPreferredAction](pencilpreferredaction.md)
  An action that the user prefers to perform after double-tapping their Apple Pencil.
- [struct PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md)
  Describes the value of an Apple Pencil double-tap gesture.
- [struct PencilSqueezeGestureValue](pencilsqueezegesturevalue.md)
  Describes the value of an Apple Pencil squeeze gesture.
- [enum PencilSqueezeGesturePhase](pencilsqueezegesturephase.md)
  Describes the phase and value of an Apple Pencil squeeze gesture.
- [struct PencilHoverPose](pencilhoverpose.md)
  A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/preferredpencilsqueezeaction)*