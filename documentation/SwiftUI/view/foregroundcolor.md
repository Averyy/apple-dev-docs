# foregroundColor(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the color of the foreground elements displayed by this view.

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
func foregroundColor(_ color: Color?) -> some View
```

## Mentions

- [Configuring views](configuring-views.md)

#### Return Value

A view that uses the foreground color you supply.

## Parameters

- `color`: The foreground color to use when displaying this   view. Pass   to remove any custom foreground color and to allow   the system or the container to provide its own foreground color.   If a container-specific override doesn’t exist, the system uses   the primary color.

## See Also

- [func colorScheme(ColorScheme) -> some View](view/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](view/listrowplattercolor(_:).md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](view/background(_:alignment:).md)
  Layers the given view behind this view.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](view/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func complicationForeground() -> some View](view/complicationforeground.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/foregroundcolor(_:))*