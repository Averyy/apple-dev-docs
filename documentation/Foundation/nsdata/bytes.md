# bytes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) const void * bytes;
```

#### Discussion

If the [`length`](./length.md) of the [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object is 0, this property returns `nil`.

For an immutable data object, the returned pointer is valid until the data object is deallocated. For a mutable data object, the returned pointer is valid until the data object is deallocated or the data is mutated.

## See Also

### Related Documentation
- [var description: String](./description.md)
  A string that contains a hexadecimal representation of the data object’s contents in a property list format.
### Accessing Underlying Bytes
- [func enumerateBytes((UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebytes%28_%29.md)
  Enumerates each range of bytes in the data object using a block.
- [func getBytes(UnsafeMutableRawPointer)](./getbytes%28_%29.md)
  Copies a data object’s contents into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](./getbytes%28_,length%29.md)
  Copies a number of bytes from the start of the data object into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](./getbytes%28_,range%29.md)
  Copies a range of bytes from the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/bytes)*