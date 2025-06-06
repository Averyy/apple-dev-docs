# monospacedDigit()

**Framework**: SwiftUI  
**Kind**: method

Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.

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
func monospacedDigit() -> Font
```

#### Return Value

A font that uses fixed-width numeric characters.

#### Discussion

This modifier only affects numeric characters, and leaves all other characters unchanged. If the base font doesn’t support fixed-width, or  digits, the font remains unchanged.

The following example shows two text fields arranged in a [`VStack`](vstack.md). Both text fields specify the 12-point system font, with the second adding the `monospacedDigit()` modifier to the font. Because the text includes the digit 1, normally a narrow character in proportional fonts, the second text field becomes wider than the first.

```swift
@State private var userText = "Effect of monospacing digits: 111,111."

var body: some View {
    VStack {
        TextField("Proportional", text: $userText)
            .font(.system(size: 12))
        TextField("Monospaced", text: $userText)
            .font(.system(size: 12).monospacedDigit())
    }
    .padding()
    .navigationTitle(Text("Font + monospacedDigit()"))
}
```

![A macOS window showing two text fields arranged vertically. Each](https://docs-assets.developer.apple.com/published/43f6da3f34065ab05d51b981cd5e9240/Environment-Font-monospacedDigit-1%402x.png)

## See Also

- [func bold() -> Font](font/bold.md)
  Adds bold styling to the font.
- [func italic() -> Font](font/italic.md)
  Adds italics to the font.
- [func monospaced() -> Font](font/monospaced.md)
  Returns a fixed-width font from the same family as the base font.
- [func smallCaps() -> Font](font/smallcaps.md)
  Adjusts the font to enable all small capitals.
- [func lowercaseSmallCaps() -> Font](font/lowercasesmallcaps.md)
  Adjusts the font to enable lowercase small capitals.
- [func uppercaseSmallCaps() -> Font](font/uppercasesmallcaps.md)
  Adjusts the font to enable uppercase small capitals.
- [func weight(Font.Weight) -> Font](font/weight(_:).md)
  Sets the weight of the font.
- [func width(Font.Width) -> Font](font/width(_:).md)
  Sets the width of the font.
- [struct Width](font/width.md)
  A width to use for fonts that have multiple widths.
- [func leading(Font.Leading) -> Font](font/leading(_:).md)
  Adjusts the line spacing of a font.
- [Font.Leading](font/leading.md)
  A line spacing adjustment that you can apply to a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/monospaceddigit())*