# enumerateBytes(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Enumerates each range of bytes in the data object using a block.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateBytes(_ block: (UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateByteRangesUsingBlock:(void (^)(const void *bytes, NSRange byteRange, BOOL *stop)) block;
```

#### Discussion

The enumeration block is called once for each contiguous region of memory in the receiver (once total for a contiguous [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object), until either all bytes have been enumerated, or the `stop` parameter is set to [`true`](../../Swift/true.md).

## Parameters

- `block`: The block to apply to byte ranges in the array.

  The block takes three arguments:

  - **bytes**: The bytes for the current range. This pointer is valid until the data object is deallocated.
  - **byteRange**: The range of the current data bytes.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the data. The stop argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the Block.

## See Also

### Accessing Underlying Bytes
- [var bytes: UnsafeRawPointer](./bytes.md)
  A pointer to the data object’s contents.
- [func getBytes(UnsafeMutableRawPointer)](./getbytes%28_%29.md)
  Copies a data object’s contents into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](./getbytes%28_,length%29.md)
  Copies a number of bytes from the start of the data object into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](./getbytes%28_,range%29.md)
  Copies a range of bytes from the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/enumeratebytes(_:))*