# NSMaximumStringLength

**Framework**: Foundation  
**Kind**: macro  
**Role**: Macro

Maximum number of characters in an `NSString` object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: This constant is not available in macOS 10.5 and later.

## Declaration

```c
#define NSMaximumStringLength
```

## See Also

### Deprecated
- [class func string(withCString: UnsafePointer<CChar>) -> Any?](./nsstring/string%28withcstring%29.md)
  Creates a new string using a given C-string.
- [class func string(withCString: UnsafePointer<CChar>, length: Int) -> Any?](./nsstring/string%28withcstring,length%29.md)
  Returns a string containing the characters in a given C-string.
- [class func string(withContentsOfFile: String) -> Any?](./nsstring/string%28withcontentsoffile%29.md)
  Returns a string created by reading data from the file named by a given path.
- [convenience init?(contentsOfFile: String)](./nsstring/init%28contentsoffile%29.md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`.
- [class func string(withContentsOf: URL) -> Any?](./nsstring/string%28withcontentsof%29.md)
  Returns a string created by reading data from the file named by a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](./nsstring/write%28tofile,atomically%29.md)
  Writes the contents of the receiver to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](./nsstring/write%28to,atomically%29.md)
  Writes the contents of the receiver to the location specified by a given URL.
- [func getCharacters(UnsafeMutablePointer<unichar>)](./nsstring/getcharacters%28_%29.md)
  Copies all characters from the receiver into a given buffer.
- [func cString() -> UnsafePointer<CChar>?](./nsstring/cstring%28%29.md)
  Returns a representation of the receiver as a C string in the default C-string encoding.
- [func lossyCString() -> UnsafePointer<CChar>?](./nsstring/lossycstring%28%29.md)
  Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding.
- [func cStringLength() -> Int](./nsstring/cstringlength%28%29.md)
  Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.
- [func getCString(UnsafeMutablePointer<CChar>)](./nsstring/getcstring%28_%29.md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](./nsstring/getcstring%28_,maxlength,range,remaining%29.md) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int)](./nsstring/getcstring%28_,maxlength%29.md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](./nsstring/getcstring%28_,maxlength,range,remaining%29.md) with `maxLength` as the maximum length in char-sized units, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int, range: NSRange, remaining: NSRangePointer?)](./nsstring/getcstring%28_,maxlength,range,remaining%29.md)
  Converts the receiver’s content to the default C-string encoding and stores them in a given buffer.
- [func addingPercentEscapes(using: UInt) -> String?](./nsstring/addingpercentescapes%28using%29.md)
  Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaximumstringlength)*