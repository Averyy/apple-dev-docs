# monospacedSystemFont(ofSize:weight:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a monospace version of the system font with the specified size and weight.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func monospacedSystemFont(ofSize fontSize: CGFloat, weight: NSFont.Weight) -> NSFont
```

```objc
+ (NSFont *) monospacedSystemFontOfSize:(CGFloat) fontSize weight:(NSFontWeight) weight;
```

## Return Value

A font object containing a monospace version of the system font at the specified size and weight.

## Discussion

Use the returned font for interface items that require monospaced glyphs. The returned font includes monospaced glyphs for the Latin characters and the symbols commonly found in source code. Glyphs for other symbols are usually wider or narrower than the monospaced characters. To ensure the font uses fixed spacing for all characters, apply the [`fixedAdvance`](../nsfontdescriptor/attributename/fixedadvance.md) attribute to the any strings you render.

## Parameters

- `fontSize`: The desired font size specified in points. If you specify `0.0` or a negative number for this parameter, the method returns the system font at the default size.
- `weight`: The desired weight of font lines, specified as one of the constants in [`NSFont.Weight`](./weight.md).

## See Also

### Creating System Fonts
- [class func preferredFont(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFont](./preferredfont%28fortextstyle,options%29.md)
  Returns the font associated with the text style.
- [class func systemFont(ofSize: CGFloat) -> NSFont](./systemfont%28ofsize%29.md)
  Returns the standard system font with the specified size.
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](./systemfont%28ofsize,weight%29.md)
  Returns the standard system font with the specified size and weight.
- [class func boldSystemFont(ofSize: CGFloat) -> NSFont](./boldsystemfont%28ofsize%29.md)
  Returns the standard system font in boldface type with the specified size.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/monospacedsystemfont(ofsize:weight:))*