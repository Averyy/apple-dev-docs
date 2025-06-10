# getCString(_:)

**Framework**: Foundation  
**Kind**: method

Invokes [`getCString(_:maxLength:range:remaining:)`](nsstring/getcstring(_:maxlength:range:remaining:).md) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getCString(_ bytes: UnsafeMutablePointer<CChar>)
```

#### Discussion

`buffer` must be large enough to contain the resulting C-string plus a terminating NULL character (which this method adds—`[string cStringLength]`).

Raises an `NSCharacterConversionException` if the receiver can’t be represented in the default C-string encoding without loss of information. Use [`canBeConverted(to:)`](nsstring/canbeconverted(to:).md) if necessary to check whether a string can be losslessly converted to the default C-string encoding. If it can’t, use [`lossyCString()`](nsstring/lossycstring().md) or [`data(using:allowLossyConversion:)`](nsstring/data(using:allowlossyconversion:).md) to get a C-string representation with some loss of information.

## See Also

- [func cString(using: UInt) -> UnsafePointer<CChar>?](nsstring/cstring(using:).md)
  Returns a representation of the string as a C string using a given encoding.
- [var utf8String: UnsafePointer<CChar>?](nsstring/utf8string.md)
  A null-terminated UTF8 representation of the string.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int, encoding: UInt) -> Bool](nsstring/getcstring(_:maxlength:encoding:).md)
  Converts the string to a given encoding and stores it in a buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getcstring(_:))*