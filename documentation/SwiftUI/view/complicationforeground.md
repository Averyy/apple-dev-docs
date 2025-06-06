# complicationForeground()

**Framework**: SwiftUI  
**Kind**: method

Promotes this view to the foreground in a complication.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency func complicationForeground() -> some View
```

#### Return Value

A view that is in the complication foreground.

#### Discussion

A view in the foreground will be tinted alongside other foreground views. The color for both the foreground and background layers is determined by the watch face.

## See Also

- [func colorScheme(ColorScheme) -> some View](view/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](view/listrowplattercolor(_:).md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](view/background(_:alignment:).md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](view/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](view/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/complicationforeground())*