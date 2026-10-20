# complicationForeground()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Promotes this view to the foreground in a complication.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

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

### Appearance modifiers
- [func colorScheme(ColorScheme) -> some View](./colorscheme%28_%29.md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](./listrowplattercolor%28_%29.md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](./background%28_,alignment%29.md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](./overlay%28_,alignment%29.md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](./foregroundcolor%28_%29.md)
  Sets the color of the foreground elements displayed by this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/complicationforeground())*