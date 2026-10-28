# drawAtPoint:forWidth:withFont:minFontSize:actualFontSize:lineBreakMode:baselineAdjustment:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Draws the string in a single line with the specified font and attributes, adjusting the font attributes as needed to render as much of the text as possible.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`draw(in:withAttributes:)`](./draw%28in,withattributes%29.md) instead.

## Declaration

```objc
- (CGSize) drawAtPoint:(CGPoint) point forWidth:(CGFloat) width withFont:(UIFont *) font minFontSize:(CGFloat) minFontSize actualFontSize:(CGFloat *) actualFontSize lineBreakMode:(NSLineBreakMode) lineBreakMode baselineAdjustment:(UIBaselineAdjustment) baselineAdjustment;
```

## Return Value

The size of the rendered string. The returned values may be rounded up to the nearest whole number.

## Parameters

- `point`: The location (in the coordinate system of the current graphics context) at which to draw the string. This point represents the top-left corner of the string’s bounding box.
- `width`: The maximum width of the string.
- `font`: The font to use for rendering.
- `minFontSize`: The minimum size to which the font may be reduced before resorting to truncation of the text.
- `actualFontSize`: On input, a pointer to a floating-point value. On return, this value contains the actual font size that was used to render the string.
- `lineBreakMode`: The line break options for computing the size of the string. For a list of possible values, see [`NSLineBreakMode`](../../AppKit/nslinebreakmode.md).
- `baselineAdjustment`: Specifies the vertical text-adjustment rule to use. This rule is used to determine the position of the text in cases where the text must be drawn at a smaller size.

## See Also

### Deprecated
- [class func string(withCString: UnsafePointer<CChar>) -> Any?](./string%28withcstring%29.md)
  Creates a new string using a given C-string.
- [class func string(withCString: UnsafePointer<CChar>, length: Int) -> Any?](./string%28withcstring,length%29.md)
  Returns a string containing the characters in a given C-string.
- [class func string(withContentsOfFile: String) -> Any?](./string%28withcontentsoffile%29.md)
  Returns a string created by reading data from the file named by a given path.
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`.
- [class func string(withContentsOf: URL) -> Any?](./string%28withcontentsof%29.md)
  Returns a string created by reading data from the file named by a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](./write%28tofile,atomically%29.md)
  Writes the contents of the receiver to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](./write%28to,atomically%29.md)
  Writes the contents of the receiver to the location specified by a given URL.
- [func getCharacters(UnsafeMutablePointer<unichar>)](./getcharacters%28_%29.md)
  Copies all characters from the receiver into a given buffer.
- [func cString() -> UnsafePointer<CChar>?](./cstring%28%29.md)
  Returns a representation of the receiver as a C string in the default C-string encoding.
- [func lossyCString() -> UnsafePointer<CChar>?](./lossycstring%28%29.md)
  Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding.
- [func cStringLength() -> Int](./cstringlength%28%29.md)
  Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.
- [func getCString(UnsafeMutablePointer<CChar>)](./getcstring%28_%29.md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](./getcstring%28_,maxlength,range,remaining%29.md) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int)](./getcstring%28_,maxlength%29.md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](./getcstring%28_,maxlength,range,remaining%29.md) with `maxLength` as the maximum length in char-sized units, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int, range: NSRange, remaining: NSRangePointer?)](./getcstring%28_,maxlength,range,remaining%29.md)
  Converts the receiver’s content to the default C-string encoding and stores them in a given buffer.
- [func addingPercentEscapes(using: UInt) -> String?](./addingpercentescapes%28using%29.md)
  Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/drawatpoint:forwidth:withfont:minfontsize:actualfontsize:linebreakmode:baselineadjustment:)*