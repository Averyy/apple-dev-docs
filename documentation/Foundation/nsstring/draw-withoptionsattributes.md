# draw(with:options:attributes:)

**Framework**: Foundation  
**Kind**: method

Draws the receiver with the specified options and other display characteristics of the given attributes, within the specified rectangle in the current graphics context.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func draw(with rect: NSRect, options: NSString.DrawingOptions = [], attributes: [NSAttributedString.Key : Any]? = nil)
```

#### Discussion

This method works in single-line, baseline rendering configuration by default. That is, the `rect` argument’s `origin` field specifies the rendering origin, and that point is interpreted as the baseline origin by default. If the string drawing option `NSStringDrawingUsesLineFragmentOrigin` is specified, `origin` is interpreted as the upper left corner of the line fragment rectangle, and the method behaves in multiline configuration.

The `size` field specifies the text container size. The `width` part of the size field specifies the maximum line fragment width if larger than `0.0`. The `height` defines the maximum size that can be occupied with text if larger than `0.0` and `NSStringDrawingUsesLineFragmentOrigin` is specified. If `NSStringDrawingUsesLineFragmentOrigin` is not specified, height is ignored and considered to be single-line rendering (`NSLineBreakByWordWrapping` and `NSLineBreakByCharWrapping` are treated as `NSLineBreakByClipping`).

You should only invoke this method when there is a current graphics context.

## Parameters

- `rect`: The rectangle in which to draw the string.
- `options`: String drawing options.
- `attributes`: A dictionary of text attributes to be applied to the string. These are the same attributes that can be applied to an   object, but in the case of   objects, the attributes apply to the entire string, rather than ranges within the string.

## See Also

- [class func string(withCString: UnsafePointer<CChar>) -> Any?](nsstring/string(withcstring:).md)
  Creates a new string using a given C-string.
- [convenience init?(CString: UnsafePointer<CChar>)](nsstring/init(cstring:).md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [class func string(withCString: UnsafePointer<CChar>, length: Int) -> Any?](nsstring/string(withcstring:length:).md)
  Returns a string containing the characters in a given C-string.
- [convenience init?(CString: UnsafePointer<CChar>, length: Int)](nsstring/init(cstring:length:).md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [convenience init?(CStringNoCopy: UnsafeMutablePointer<CChar>, length: Int, freeWhenDone: Bool)](nsstring/init(cstringnocopy:length:freewhendone:).md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [class func string(withContentsOfFile: String) -> Any?](nsstring/string(withcontentsoffile:).md)
  Returns a string created by reading data from the file named by a given path.
- [convenience init?(contentsOfFile: String)](nsstring/init(contentsoffile:).md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`.
- [class func string(withContentsOf: URL) -> Any?](nsstring/string(withcontentsof:).md)
  Returns a string created by reading data from the file named by a given URL.
- [convenience init?(contentsOfURL: URL)](nsstring/init(contentsofurl:).md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the location named by a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](nsstring/write(tofile:atomically:).md)
  Writes the contents of the receiver to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](nsstring/write(to:atomically:).md)
  Writes the contents of the receiver to the location specified by a given URL.
- [func getCharacters(UnsafeMutablePointer<unichar>)](nsstring/getcharacters(_:).md)
  Copies all characters from the receiver into a given buffer.
- [func cString() -> UnsafePointer<CChar>?](nsstring/cstring.md)
  Returns a representation of the receiver as a C string in the default C-string encoding.
- [func lossyCString() -> UnsafePointer<CChar>?](nsstring/lossycstring.md)
  Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding.
- [func cStringLength() -> Int](nsstring/cstringlength.md)
  Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/draw(with:options:attributes:))*