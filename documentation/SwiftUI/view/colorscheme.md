# colorScheme(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets this view’s color scheme.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func colorScheme(_ colorScheme: ColorScheme) -> some View
```

#### Return Value

A view that sets this view’s color scheme.

#### Discussion

Use `colorScheme(_:)` to set the color scheme for the view to which you apply it and any subviews.

## Parameters

- `colorScheme`: The color scheme for this view.

## See Also

- [func listRowPlatterColor(Color?) -> some View](view/listrowplattercolor(_:).md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](view/background(_:alignment:).md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](view/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](view/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](view/complicationforeground.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/colorscheme(_:))*