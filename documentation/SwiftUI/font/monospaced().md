# monospaced()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a fixed-width font from the same family as the base font.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func monospaced() -> Font
```

#### Return Value

A fixed-width font from the same family as the base font, if one is available, and a default fixed-width font otherwise.

#### Discussion

If there’s no suitable font face in the same family, SwiftUI returns a default fixed-width font.

The following example adds the `monospaced()` modifier to the default system font, then applies this font to a [`Text`](../text.md) view:

```swift
struct ContentView: View {
    let myFont = Font
        .system(size: 24)
        .monospaced()

    var body: some View {
        Text("Hello, world!")
            .font(myFont)
            .padding()
            .navigationTitle("Monospaced")
    }
}
```

![A macOS window showing the text Hello, world in a 24-point](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Environment-Font-monospaced-1@2x.png)

SwiftUI may provide different fixed-width replacements for standard user interface fonts (such as [`title`](./title.md), or a system font created with [`system(_:design:)`](./system%28_,design%29.md)) than for those same fonts when created by name with [`custom(_:size:)`](./custom%28_,size%29.md).

The [`font(_:)`](../view/font%28_%29.md) modifier applies the font to all text within the view. To mix fixed-width text with other styles in the same `Text` view, use the [`init(_:)`](../text/init%28_%29-1a4oh.md) initializer to use an appropropriately-styled [`AttributedString`](../../Foundation/attributedstring.md) for the text view’s content. You can use the [`init(markdown:options:baseURL:)`](../../Foundation/attributedstring/init%28markdown,options,baseurl%29-52n3u.md) initializer to provide a Markdown-formatted string containing the backtick-syntax (`…`) to apply code voice to specific ranges of the attributed string.

## See Also

### Styling a font
- [func bold() -> Font](./bold%28%29.md)
  Adds bold or emphasized styling to the font.
- [func italic() -> Font](./italic%28%29.md)
  Adds italics to the font.
- [func monospacedDigit() -> Font](./monospaceddigit%28%29.md)
  Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [func smallCaps() -> Font](./smallcaps%28%29.md)
  Adjusts the font to enable all small capitals.
- [func lowercaseSmallCaps() -> Font](./lowercasesmallcaps%28%29.md)
  Adjusts the font to enable lowercase small capitals.
- [func uppercaseSmallCaps() -> Font](./uppercasesmallcaps%28%29.md)
  Adjusts the font to enable uppercase small capitals.
- [func weight(Font.Weight) -> Font](./weight%28_%29.md)
  Sets the weight of the font.
- [func width(Font.Width) -> Font](./width%28_%29.md)
  Sets the width of the font.
- [struct Width](./width.md)
  A width to use for fonts that have multiple widths.
- [func leading(Font.Leading) -> Font](./leading%28_%29.md)
  Adjusts the line spacing of a font.
- [Font.Leading](./leading.md)
  A line spacing adjustment that you can apply to a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/monospaced())*