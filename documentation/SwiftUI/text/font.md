# font(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the default font for text in the view.

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
func font(_ font: Font?) -> Text
```

## Mentions

- [Applying custom fonts to text](applying-custom-fonts-to-text.md)

#### Return Value

Text that uses the font you specify.

#### Discussion

Use `font(_:)` to apply a specific font to an individual Text View, or all of the text views in a container.

In the example below, the first text field has a font set directly, while the font applied to the following container applies to all of the text views inside that container:

```swift
VStack {
    Text("Font applied to a text view.")
        .font(.largeTitle)

    VStack {
        Text("These two text views have the same font")
        Text("applied to their parent view.")
    }
    .font(.system(size: 16, weight: .light, design: .default))
}
```

![Applying a font to a single text view or a view container](https://docs-assets.developer.apple.com/published/96bbeed6b182bf19c533efcca8a5fcaa/SwiftUI-view-font%402x.png)

## Parameters

- `font`: The font to use when displaying this text.

## See Also

- [func fontWeight(Font.Weight?) -> Text](text/fontweight(_:).md)
  Sets the font weight of the text.
- [func fontDesign(Font.Design?) -> Text](text/fontdesign(_:).md)
  Sets the font design of the text.
- [func fontWidth(Font.Width?) -> Text](text/fontwidth(_:).md)
  Sets the font width of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/font(_:))*