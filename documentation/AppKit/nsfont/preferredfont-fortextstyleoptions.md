# preferredFont(forTextStyle:options:)

**Framework**: AppKit  
**Kind**: method

Returns the font associated with the text style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func preferredFont(forTextStyle style: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any] = [:]) -> NSFont
```

#### Return Value

The font associated with the text style.

#### Discussion

> **Note**:  Session 10058: [`What’s new with text and text interactions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10058/)

#### Discussion

A font’s metrics, such as [`ascender`](nsfont/ascender.md), [`descender`](nsfont/descender.md), and [`leading`](nsfont/leading.md), can differ across devices for the same text style and point size. AppKit reserves extra vertical space to accommodate scripts like Thai and Hindi whenever someone includes one of those languages in their preferred languages, even if your text doesn’t use that script.

To take advantage of this behavior, create a font explicitly with this method and assign it to a text element. Don’t clip these text elements: ascenders and descenders for languages like Thai and Hindi often protrude beyond the expected line height. This typically isn’t a problem, since layouts usually leave extra space around neighboring elements, but clipping the view clips that text.

## Parameters

- `style`: The text style for which to return a font. See [`NSFont.TextStyle`](nsfont/textstyle.md) for available values.
- `options`: A dictionary you use to further configure the returned font. See [`NSFont.TextStyleOptionKey`](nsfont/textstyleoptionkey.md) for a list of valid keys. Pass an empty dictionary to use the default configuration.

## See Also

- [class func systemFont(ofSize: CGFloat) -> NSFont](nsfont/systemfont(ofsize:).md)
  Returns the standard system font with the specified size.
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/systemfont(ofsize:weight:).md)
  Returns the standard system font with the specified size and weight.
- [class func boldSystemFont(ofSize: CGFloat) -> NSFont](nsfont/boldsystemfont(ofsize:).md)
  Returns the standard system font in boldface type with the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/monospacedsystemfont(ofsize:weight:).md)
  Returns a monospace version of the system font with the specified size and weight.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/monospaceddigitsystemfont(ofsize:weight:).md)
  Returns a version of the standard system font that contains monospaced digit glyphs.
- [class var systemFontSize: CGFloat](nsfont/systemfontsize.md)
  Returns the size of the standard system font.
- [class var smallSystemFontSize: CGFloat](nsfont/smallsystemfontsize.md)
  Returns the size of the standard small system font.
- [NSFont.Weight](nsfont/weight.md)
  System-defined font-weight values.
- [NSFont.TextStyle](nsfont/textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSFont.TextStyleOptionKey](nsfont/textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/preferredfont(fortextstyle:options:))*