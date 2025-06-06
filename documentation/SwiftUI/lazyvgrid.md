# LazyVGrid

**Framework**: SwiftUI  
**Kind**: struct

A container view that arranges its child views in a grid that grows vertically, creating items only as needed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct LazyVGrid<Content> where Content : View
```

## Mentions

- [Picking container views for your content](picking-container-views-for-your-content.md)

#### Overview

Use a lazy vertical grid when you want to display a large, vertically scrollable collection of views arranged in a two dimensional layout. The first view that you provide to the grid’s `content` closure appears in the top row of the column that’s on the grid’s leading edge. Additional views occupy successive cells in the grid, filling the first row from leading to trailing edges, then the second row, and so on. The number of rows can grow unbounded, but you specify the number of columns by providing a corresponding number of [`GridItem`](griditem.md) instances to the grid’s initializer.

The grid in the following example defines two columns and uses a [`ForEach`](foreach.md) structure to repeatedly generate a pair of [`Text`](text.md) views for the columns in each row:

```swift
struct VerticalSmileys: View {
    let columns = [GridItem(.flexible()), GridItem(.flexible())]

    var body: some View {
         ScrollView {
             LazyVGrid(columns: columns) {
                 ForEach(0x1f600...0x1f679, id: \.self) { value in
                     Text(String(format: "%x", value))
                     Text(emoji(value))
                         .font(.largeTitle)
                 }
             }
         }
    }

    private func emoji(_ value: Int) -> String {
        guard let scalar = UnicodeScalar(value) else { return "?" }
        return String(Character(scalar))
    }
}
```

For each row in the grid, the first column shows a Unicode code point from the “Smileys” group, and the second shows its corresponding emoji:

![A screenshot of a colunb of hexadecimal numbers to the left of a column](https://docs-assets.developer.apple.com/published/fe2b80b65b59918ba760ae0b7c36e15c/LazyVGrid-1-iOS%402x.png)

You can achieve a similar layout using a [`Grid`](grid.md) container. Unlike a lazy grid, which creates child views only when SwiftUI needs to display them, a regular grid creates all of its child views right away. This enables the grid to provide better support for cell spacing and alignment. Only use a lazy grid if profiling your app shows that a [`Grid`](grid.md) view performs poorly because it tries to load too many views at once.

## Topics

### Creating a vertical grid
- [init(columns: [GridItem], alignment: HorizontalAlignment, spacing: CGFloat?, pinnedViews: PinnedScrollableViews, content: () -> Content)](lazyvgrid/init(columns:alignment:spacing:pinnedviews:content:).md)
  Creates a grid that grows vertically.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct LazyHGrid](lazyhgrid.md)
  A container view that arranges its child views in a grid that grows horizontally, creating items only as needed.
- [struct GridItem](griditem.md)
  A description of a row or a column in a lazy grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazyvgrid)*