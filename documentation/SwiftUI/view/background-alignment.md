# background(_:alignment:)

**Framework**: SwiftUI  
**Kind**: method

Layers the given view behind this view.

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
func background<Background>(_ background: Background, alignment: Alignment = .center) -> some View where Background : View
```

## Mentions

- [Adding a background to your view](adding-a-background-to-your-view.md)
- [Building layouts with stack views](building-layouts-with-stack-views.md)

#### Discussion

Use `background(_:alignment:)` when you need to place one view behind another, with the background view optionally aligned with a specified edge of the frontmost view.

The example below creates two views: the `Frontmost` view, and the `DiamondBackground` view. The `Frontmost` view uses the `DiamondBackground` view for the background of the image element inside the `Frontmost` view’s [`VStack`](vstack.md).

```swift
struct DiamondBackground: View {
    var body: some View {
        VStack {
            Rectangle()
                .fill(Color.gray)
                .frame(width: 250, height: 250, alignment: .center)
                .rotationEffect(.degrees(45.0))
        }
    }
}

struct Frontmost: View {
    var body: some View {
        VStack {
            Image(systemName: "folder")
                .font(.system(size: 128, weight: .ultraLight))
                .background(DiamondBackground())
        }
    }
}
```

![A view showing a large folder image with a gray diamond placed behind it as its background view.](https://docs-assets.developer.apple.com/published/2f4e39d1360323a046bdf9d567b2600a/View-background-1%402x.png)

## Parameters

- `background`: The view to draw behind this view.
- `alignment`: The alignment with a default value of    that you use to position the background view.

## See Also

- [func colorScheme(ColorScheme) -> some View](view/colorscheme(_:).md)
  Sets this view’s color scheme.
- [func listRowPlatterColor(Color?) -> some View](view/listrowplattercolor(_:).md)
  Sets the color that the system applies to the row background when this view is placed in a list.
- [func overlay<Overlay>(Overlay, alignment: Alignment) -> some View](view/overlay(_:alignment:).md)
  Layers a secondary view in front of this view.
- [func foregroundColor(Color?) -> some View](view/foregroundcolor(_:).md)
  Sets the color of the foreground elements displayed by this view.
- [func complicationForeground() -> some View](view/complicationforeground.md)
  Promotes this view to the foreground in a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(_:alignment:))*