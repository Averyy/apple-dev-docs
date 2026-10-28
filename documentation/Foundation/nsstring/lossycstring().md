# lossyCString()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`cString(using:)`](./cstring%28using%29.md) or [`data(using:allowLossyConversion:)`](./data%28using,allowlossyconversion%29.md) instead.

## Declaration

```swift
func lossyCString() -> UnsafePointer<CChar>?
```

```objc
- (const char *) lossyCString;
```

## Discussion

This method does not raise an exception if the conversion is lossy. The returned C string will be automatically freed just as a returned object would be released; your code should copy the C string or use [`getCString(_:)`](./getcstring%28_%29.md) if it needs to store the C string outside of the autorelease context in which the C string is created.

## See Also

### Related Documentation
- [func cString(using: UInt) -> UnsafePointer<CChar>?](./cstring%28using%29.md)
  Returns a representation of the string as a C string using a given encoding.
- [func data(using: UInt, allowLossyConversion: Bool) -> Data?](./data%28using,allowlossyconversion%29.md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
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
- [func cStringLength() -> Int](./cstringlength%28%29.md)
  Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.
- [func getCString(UnsafeMutablePointer<CChar>)](./getcstring%28_%29.md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](./getcstring%28_,maxlength,range,remaining%29.md) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [- getCString:maxLength:](./getcstring%28_,maxlength%29.md)
  Invokes [`getCString:maxLength:range:remainingRange:`](./getcstring%28_,maxlength,range,remaining%29.md) with `maxLength` as the maximum length in char-sized units, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [- getCString:maxLength:range:remainingRange:](./getcstring%28_,maxlength,range,remaining%29.md)
  Converts the receiver’s content to the default C-string encoding and stores them in a given buffer.
- [- stringByAddingPercentEscapesUsingEncoding:](./addingpercentescapes%28using%29.md)
  Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string.
- [- stringByReplacingPercentEscapesUsingEncoding:](./replacingpercentescapes%28using%29.md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/lossycstring())*