# replacingPercentEscapes(using:)

**Framework**: Foundation  
**Kind**: method

Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func replacingPercentEscapes(using enc: UInt) -> String?
```

#### Return Value

A new string made by replacing in the receiver all percent escapes with the matching characters as determined by the given encoding `encoding`. Returns `nil` if the transformation is not possible, for example, the percent escapes give a byte sequence not legal in `encoding`.

#### Discussion

See [`CFURLCreateStringByReplacingPercentEscapes(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLCreateStringByReplacingPercentEscapes(_:_:_:)) for more complex transformations.

## Parameters

- `enc`: The encoding to use for the returned string.

## See Also

- [func addingPercentEncoding(withAllowedCharacters: CharacterSet) -> String?](nsstring/addingpercentencoding(withallowedcharacters:).md)
  Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.
- [var removingPercentEncoding: String?](nsstring/removingpercentencoding.md)
  Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/replacingpercentescapes(using:))*