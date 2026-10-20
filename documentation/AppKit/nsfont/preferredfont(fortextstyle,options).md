# preferredFont(forTextStyle:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the font associated with the text style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class func preferredFont(forTextStyle style: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any] = [:]) -> NSFont
```

```objc
+ (NSFont *) preferredFontForTextStyle:(NSFontTextStyle) style options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

The font associated with the text style.

#### Discussion

> **Related sessions from WWDC23**:  Session 10058: [What’s new with text and text interactions](https://developer.apple.com/videos/play/wwdc2023/10058/)

#### Discussion

A font’s metrics, such as [`ascender`](./ascender.md), [`descender`](./descender.md), and [`leading`](./leading.md), can differ across devices for the same text style and point size. AppKit reserves extra vertical space to accommodate scripts like Thai and Hindi whenever someone includes one of those languages in their preferred languages, even if your text doesn’t use that script.

To take advantage of this behavior, create a font explicitly with this method and assign it to a text element. Don’t clip these text elements: ascenders and descenders for languages like Thai and Hindi often protrude beyond the expected line height. This typically isn’t a problem, since layouts usually leave extra space around neighboring elements, but clipping the view clips that text.

## Parameters

- `style`: The text style for which to return a font. See [`NSFont.TextStyle`](./textstyle.md) for available values.
- `options`: A dictionary you use to further configure the returned font. See [`NSFont.TextStyleOptionKey`](./textstyleoptionkey.md) for a list of valid keys. Pass an empty dictionary to use the default configuration.

## See Also

### Creating System Fonts
- [class func systemFont(ofSize: CGFloat) -> NSFont](./systemfont%28ofsize%29.md)
  Returns the standard system font with the specified size.
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](./systemfont%28ofsize,weight%29.md)
  Returns the standard system font with the specified size and weight.
- [class func boldSystemFont(ofSize: CGFloat) -> NSFont](./boldsystemfont%28ofsize%29.md)
  Returns the standard system font in boldface type with the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](./monospacedsystemfont%28ofsize,weight%29.md)
  Returns a monospace version of the system font with the specified size and weight.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](./monospaceddigitsystemfont%28ofsize,weight%29.md)
  Returns a version of the standard system font that contains monospaced digit glyphs.
- [class var systemFontSize: CGFloat](./systemfontsize.md)
  Returns the size of the standard system font.
- [class var smallSystemFontSize: CGFloat](./smallsystemfontsize.md)
  Returns the size of the standard small system font.
- [NSFont.Weight](./weight.md)
  System-defined font-weight values.
- [NSFont.TextStyle](./textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSFont.TextStyleOptionKey](./textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/preferredfont(fortextstyle:options:))*