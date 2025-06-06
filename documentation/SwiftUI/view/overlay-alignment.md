# overlay(_:alignment:)

**Framework**: SwiftUI  
**Kind**: method

Layers a secondary view in front of this view.

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
func overlay<Overlay>(_ overlay: Overlay, alignment: Alignment = .center) -> some View where Overlay : View
```

## Mentions

- [Building layouts with stack views](building-layouts-with-stack-views.md)

#### Return Value

A view that layers `overlay` in front of the view.

#### Discussion

When you apply an overlay to a view, the original view continues to provide the layout characteristics for the resulting view. In the following example, the heart image is shown overlaid in front of, and aligned to the bottom of the folder image.

```swift
Image(systemName: "folder")
    .font(.system(size: 55, weight: .thin))
    .overlay(Text("❤️"), alignment: .bottom)
```

![View showing placement of a heart overlaid onto a folder icon.](https://docs-assets.developer.apple.com/published/4f0a125e7d66518fa559f8899e888853/View-overlay-1%402x.png)

## Parameters

- `overlay`: The view to layer in front of this view.
- `alignment`: The alignment for   in relation to this view.

## See Also

- [func colorScheme(ColorScheme) -> some View](view/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](view/listrowplattercolor(_:).md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](view/background(_:alignment:).md)
  Layers the given view behind this view.
- [func foregroundColor(Color?) -> some View](view/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](view/complicationforeground.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/overlay(_:alignment:))*