# bytes

**Framework**: Foundation  
**Kind**: property

A pointer to the data object’s contents.

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
var bytes: UnsafeRawPointer { get }
```

#### Discussion

If the [`length`](nsdata/length.md) of the [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object is 0, this property returns `nil`.

For an immutable data object, the returned pointer is valid until the data object is deallocated. For a mutable data object, the returned pointer is valid until the data object is deallocated or the data is mutated.

## See Also

- [var description: String](nsdata/description.md)
  A string that contains a hexadecimal representation of the data object’s contents in a property list format.
- [func enumerateBytes((UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdata/enumeratebytes(_:).md)
  Enumerates each range of bytes in the data object using a block.
- [func getBytes(UnsafeMutableRawPointer)](nsdata/getbytes(_:).md)
  Copies a data object’s contents into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](nsdata/getbytes(_:length:).md)
  Copies a number of bytes from the start of the data object into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](nsdata/getbytes(_:range:).md)
  Copies a range of bytes from the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/bytes)*