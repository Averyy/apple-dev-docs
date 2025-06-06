# getBytes(_:range:)

**Framework**: Foundation  
**Kind**: method

Copies a range of bytes from the data object into a given buffer.

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
func getBytes(_ buffer: UnsafeMutableRawPointer, range: NSRange)
```

#### Discussion

If `range` isn’t within the receiver’s range of bytes, an [`rangeException`](nsexceptionname/rangeexception.md) is raised.

## Parameters

- `buffer`: A buffer into which to copy data.
- `range`: The range of bytes in the receiver’s data to copy to  . The range must lie within the range of bytes of the receiver’s data.

## See Also

- [var description: String](nsdata/description.md)
  A string that contains a hexadecimal representation of the data object’s contents in a property list format.
- [var bytes: UnsafeRawPointer](nsdata/bytes.md)
  A pointer to the data object’s contents.
- [func enumerateBytes((UnsafeRawPointer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdata/enumeratebytes(_:).md)
  Enumerates each range of bytes in the data object using a block.
- [func getBytes(UnsafeMutableRawPointer)](nsdata/getbytes(_:).md)
  Copies a data object’s contents into a given buffer.
- [func getBytes(UnsafeMutableRawPointer, length: Int)](nsdata/getbytes(_:length:).md)
  Copies a number of bytes from the start of the data object into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/getbytes(_:range:))*