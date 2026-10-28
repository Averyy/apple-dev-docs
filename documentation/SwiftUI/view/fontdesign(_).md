# fontDesign(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the font design of the text in this view.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
nonisolated
func fontDesign(_ design: Font.Design?) -> some View
```

## Return Value

A view that uses the font design you specify.

## Parameters

- `design`: One of the available font designs. Providing `nil` removes the effect of any font design modifier applied higher in the view hierarchy.

## See Also

### Setting a font
- [Applying custom fonts to text](../applying-custom-fonts-to-text.md)
  Add and use a font in your app that scales with Dynamic Type.
- [func font(Font?) -> some View](./font%28_%29.md)
  Sets the default font for text in this view.
- [func fontWeight(Font.Weight?) -> some View](./fontweight%28_%29.md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](./fontwidth%28_%29.md)
  Sets the font width of the text in this view.
- [var font: Font?](../environmentvalues/font.md)
  The default font of this environment.
- [struct Font](../font.md)
  An environment-dependent font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fontdesign(_:))*