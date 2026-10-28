# getBytes(_:length:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies a number of bytes from the start of the data object into a given buffer.

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
func getBytes(_ buffer: UnsafeMutableRawPointer, length: Int)
```

```objc
- (void) getBytes:(void *) buffer length:(NSUInteger) length;
```

## Discussion

The number of bytes copied is the smaller of the `length` parameter and the [`length`](./length.md) of the data encapsulated in the object.

## Parameters

- `buffer`: A buffer into which to copy data.
- `length`: The number of bytes from the start of the receiver’s data to copy to `buffer`.

## See Also

### Related Documentation
- [var description: String](./description.md)
  A string that contains a hexadecimal representation of the data object’s contents in a property list format.
### Accessing Underlying Bytes
- [var bytes: UnsafeRawPointer](./bytes.md)
  A pointer to the data object’s contents.
- [func enumerateBytes((UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebytes%28_%29.md)
  Enumerates each range of bytes in the data object using a block.
- [func getBytes(UnsafeMutableRawPointer)](./getbytes%28_%29.md)
  Copies a data object’s contents into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](./getbytes%28_,range%29.md)
  Copies a range of bytes from the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/getbytes(_:length:))*