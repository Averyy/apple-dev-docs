# addingPercentEscapes(using:)

**Framework**: Foundation  
**Kind**: method

Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string.

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
func addingPercentEscapes(using enc: UInt) -> String?
```

#### Return Value

A representation of the receiver using `encoding` to determine the percent escapes necessary to convert the receiver into a legal URL string. Returns `nil` if `encoding` cannot encode a particular character.

#### Discussion

It may be difficult to use this function to “clean up” unescaped or partially escaped URL strings where sequences are unpredictable. See [`CFURLCreateStringByAddingPercentEscapes(_:_:_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLCreateStringByAddingPercentEscapes(_:_:_:_:_:)) for more information.

## Parameters

- `enc`: The encoding to use for the returned string. If you are uncertain of the correct encoding you should use  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/addingpercentescapes(using:))*