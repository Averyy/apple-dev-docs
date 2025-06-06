# enumerateBytes(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

The enumeration block is called once for each contiguous region of memory in the receiver (once total for a contiguous [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object), until either all bytes have been enumerated, or the `stop` parameter is set to [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `block`: The block takes three arguments:

## See Also

- [var bytes: UnsafeRawPointer](nsdata/bytes.md)
  A pointer to the data object’s contents.
- [func getBytes(UnsafeMutableRawPointer)](nsdata/getbytes(_:).md)
  Copies a data object’s contents into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](nsdata/getbytes(_:length:).md)
  Copies a number of bytes from the start of the data object into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, range: NSRange)](nsdata/getbytes(_:range:).md)
  Copies a range of bytes from the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/enumeratebytes(_:))*