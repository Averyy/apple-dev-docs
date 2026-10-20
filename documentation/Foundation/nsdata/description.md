# description

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string that contains a hexadecimal representation of the data object’s contents in a property list format.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var description: String { get }
```

```objc
@property (copy, readonly) NSString * description;
```

## See Also

### Related Documentation
- [func getBytes(UnsafeMutableRawPointer)](./getbytes%28_%29.md)
  Copies a data object’s contents into a given buffer.
- [var bytes: UnsafeRawPointer](./bytes.md)
  A pointer to the data object’s contents.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](./getbytes%28_,range%29.md)
  Copies a range of bytes from the data object into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](./getbytes%28_,length%29.md)
  Copies a number of bytes from the start of the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/description)*