# write(toFile:atomically:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the contents of the receiver to the file specified by a given path.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`write(toFile:atomically:encoding:)`](./write%28tofile,atomically,encoding%29.md) instead.

## Declaration

```swift
func write(toFile path: String, atomically useAuxiliaryFile: Bool) -> Bool
```

```objc
- (BOOL) writeToFile:(NSString *) path atomically:(BOOL) useAuxiliaryFile;
```

#### Return Value

[`true`](../../Swift/true.md) if the file is written successfully, otherwise [`false`](../../Swift/false.md).

#### Discussion

Writes the contents of the receiver to the file specified by `path` (overwriting any existing file at `path`). `path` is written in the default C-string encoding if possible (that is, if no information would be lost), in the Unicode encoding otherwise.

If `flag` is [`true`](../../Swift/true.md), the receiver is written to an auxiliary file, and then the auxiliary file is renamed to `path`. If `flag` is [`false`](../../Swift/false.md), the receiver is written directly to `path`. The [`true`](../../Swift/true.md) option guarantees that `path`, if it exists at all, won’t be corrupted even if the system should crash during writing.

If `path` contains a tilde (`~`) character, you must expand it with [`expandingTildeInPath`](./expandingtildeinpath.md) before invoking this method.

## See Also

### Related Documentation
- [func write(toFile: String, atomically: Bool, encoding: UInt) throws](./write%28tofile,atomically,encoding%29.md)
  Writes the contents of the receiver to a file at a given path using a given encoding.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/write(tofile:atomically:))*