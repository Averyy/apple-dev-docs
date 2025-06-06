# fontWidth(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the font width of the text in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func fontWidth(_ width: Font.Width?) -> some View
```

#### Return Value

A view that uses the font width you specify.

## Parameters

- `width`: One of the available font widths.   Providing   removes the effect of any font width   modifier applied higher in the view hierarchy.

## See Also

- [Applying custom fonts to text](applying-custom-fonts-to-text.md)
  Add and use a font in your app that scales with Dynamic Type.
- [func font(Font?) -> some View](view/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](view/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](view/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [var font: Font?](environmentvalues/font.md)
  The default font of this environment.
- [struct Font](font.md)
  An environment-dependent font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fontwidth(_:))*