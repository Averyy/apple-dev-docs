# sizeWithFont:forWidth:lineBreakMode:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the size of the string if it were to be rendered with the specified font and line attributes on a single line.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`boundingRect(with:options:attributes:context:)`](./boundingrect%28with,options,attributes,context%29.md).

## Declaration

```objc
- (CGSize) sizeWithFont:(UIFont *) font forWidth:(CGFloat) width lineBreakMode:(NSLineBreakMode) lineBreakMode;
```

## Return Value

The width and height of the resulting string’s bounding box. These values may be rounded up to the nearest whole number.

## Discussion

You can use this method to obtain the layout metrics you need to draw a string in your user interface. This method does not actually draw the string or alter the receiver’s text in any way.

This method returns the width and height of the string constrained to the specified width. Although it computes where line breaks would occur, this method does not actually wrap the text to additional lines. If the size of the string exceeds the given width, this method truncates the text (for layout purposes only) using the specified line break mode until it does conform to the maximum width; it then returns the size of the resulting truncated string.

## Parameters

- `font`: The font to use for computing the string size.
- `width`: The maximum acceptable width for the string. This value is used to calculate where line breaks would be placed.
- `lineBreakMode`: The line break options for computing the size of the string. For a list of possible values, see [`NSLineBreakMode`](../../AppKit/nslinebreakmode.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/sizewithfont:forwidth:linebreakmode:)*