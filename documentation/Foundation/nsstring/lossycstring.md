# lossyCString()

**Framework**: Foundation  
**Kind**: method

Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func lossyCString() -> UnsafePointer<CChar>?
```

#### Discussion

This method does not raise an exception if the conversion is lossy. The returned C string will be automatically freed just as a returned object would be released; your code should copy the C string or use [`getCString(_:)`](nsstring/getcstring(_:).md) if it needs to store the C string outside of the autorelease context in which the C string is created.

## See Also

- [func cString(using: UInt) -> UnsafePointer<CChar>?](nsstring/cstring(using:).md)
  Returns a representation of the string as a C string using a given encoding.
- [func data(using: UInt, allowLossyConversion: Bool) -> Data?](nsstring/data(using:allowlossyconversion:).md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
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
- [func cStringLength() -> Int](nsstring/cstringlength.md)
  Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.
- [func getCString(UnsafeMutablePointer<CChar>)](nsstring/getcstring(_:).md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](nsstring/getcstring(_:maxlength:range:remaining:).md) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/lossycstring())*