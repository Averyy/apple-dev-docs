# overlay(_:alignment:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Layers a secondary view in front of this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`overlay(alignment:content:)`](./overlay%28alignment,content%29.md) instead.

## Declaration

```swift
nonisolated
func overlay<Overlay>(_ overlay: Overlay, alignment: Alignment = .center) -> some View where Overlay : View
```

## Mentions

- [Building layouts with stack views](../building-layouts-with-stack-views.md)

## Return Value

A view that layers `overlay` in front of the view.

## Discussion

When you apply an overlay to a view, the original view continues to provide the layout characteristics for the resulting view. In the following example, the heart image is shown overlaid in front of, and aligned to the bottom of the folder image.

```swift
Image(systemName: "folder")
    .font(.system(size: 55, weight: .thin))
    .overlay(Text("❤️"), alignment: .bottom)
```

![View showing placement of a heart overlaid onto a folder icon.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-overlay-1@2x.png)

## Parameters

- `overlay`: The view to layer in front of this view.
- `alignment`: The alignment for `overlay` in relation to this view.

## See Also

### Appearance modifiers
- [func colorScheme(ColorScheme) -> some View](./colorscheme%28_%29.md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](./listrowplattercolor%28_%29.md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func background<Background>(Background, alignment: Alignment) -> some View](./background%28_,alignment%29.md)
  Layers the given view behind this view.
- [func foregroundColor(Color?) -> some View](./foregroundcolor%28_%29.md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](./complicationforeground%28%29.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/overlay(_:alignment:))*