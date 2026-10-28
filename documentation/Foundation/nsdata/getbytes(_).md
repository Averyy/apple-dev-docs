# getBytes(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies a data object’s contents into a given buffer.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: This method is unsafe because it could potentially cause buffer overruns. Use [`getBytes(_:length:)`](./getbytes%28_,length%29.md) or [`getBytes(_:range:)`](./getbytes%28_,range%29.md) instead.

## Declaration

```swift
func getBytes(_ buffer: UnsafeMutableRawPointer)
```

```objc
- (void) getBytes:(void *) buffer;
```

## Discussion

You can see a sample using this method in [Working With Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingBinaryData.html#//apple_ref/doc/uid/20000717).

## Parameters

- `buffer`: A buffer into which to copy the receiver’s data. The buffer must be at least [`length`](./length.md) bytes.

## See Also

### Related Documentation
- [var description: String](./description.md)
  A string that contains a hexadecimal representation of the data object’s contents in a property list format.
### Accessing Underlying Bytes
- [var bytes: UnsafeRawPointer](./bytes.md)
  A pointer to the data object’s contents.
- [func enumerateBytes((UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratebytes%28_%29.md)
  Enumerates each range of bytes in the data object using a block.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](./getbytes%28_,length%29.md)
  Copies a number of bytes from the start of the data object into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](./getbytes%28_,range%29.md)
  Copies a range of bytes from the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/getbytes(_:))*