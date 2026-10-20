# getCString(_:maxLength:range:remaining:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Converts the receiver’s content to the default C-string encoding and stores them in a given buffer.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`getCString(_:maxLength:encoding:)`](./getcstring%28_,maxlength,encoding%29.md) instead.

## Declaration

```swift
func getCString(_ bytes: UnsafeMutablePointer<CChar>, maxLength: Int, range aRange: NSRange, remaining leftoverRange: NSRangePointer?)
```

```objc
- (void) getCString:(char *) bytes maxLength:(NSUInteger) maxLength range:(NSRange) aRange remainingRange:(NSRangePointer) leftoverRange;
```

#### Discussion

`buffer` must be large enough to contain `maxLength` bytes plus a terminating zero character (which this method adds). Copies and converts as many characters as possible from `aRange` and stores the range of those not converted in the range given by `leftoverRange` (if it’s non-`nil`). Raises an `NSRangeException` if any part of `aRange` lies beyond the end of the string.

Raises an `NSCharacterConversionException` if the receiver can’t be represented in the default C-string encoding without loss of information. Use [`canBeConverted(to:)`](./canbeconverted%28to%29.md) if necessary to check whether a string can be losslessly converted to the default C-string encoding. If it can’t, use [`lossyCString()`](./lossycstring%28%29.md) or [`data(using:allowLossyConversion:)`](./data%28using,allowlossyconversion%29.md) to get a C-string representation with some loss of information.

## See Also

### Related Documentation
- [func cString(using: UInt) -> UnsafePointer<CChar>?](./cstring%28using%29.md)
  Returns a representation of the string as a C string using a given encoding.
- [var utf8String: UnsafePointer<CChar>?](./utf8string.md)
  A null-terminated UTF8 representation of the string.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int, encoding: UInt) -> Bool](./getcstring%28_,maxlength,encoding%29.md)
  Converts the string to a given encoding and stores it in a buffer.
### Deprecated
- [class func string(withCString: UnsafePointer<CChar>) -> Any?](./string%28withcstring%29.md)
  Creates a new string using a given C-string.
- [convenience init?(CString: UnsafePointer<CChar>)](./init%28cstring%29-vkuo.md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [class func string(withCString: UnsafePointer<CChar>, length: Int) -> Any?](./string%28withcstring,length%29.md)
  Returns a string containing the characters in a given C-string.
- [convenience init?(CString: UnsafePointer<CChar>, length: Int)](./init%28cstring,length%29-5ure3.md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [convenience init?(CStringNoCopy: UnsafeMutablePointer<CChar>, length: Int, freeWhenDone: Bool)](./init%28cstringnocopy,length,freewhendone%29-86dm2.md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [class func string(withContentsOfFile: String) -> Any?](./string%28withcontentsoffile%29.md)
  Returns a string created by reading data from the file named by a given path.
- [convenience init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`.
- [class func string(withContentsOf: URL) -> Any?](./string%28withcontentsof%29.md)
  Returns a string created by reading data from the file named by a given URL.
- [convenience init?(contentsOfURL: URL)](./init%28contentsofurl%29.md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the location named by a given URL.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getcstring(_:maxlength:range:remaining:))*