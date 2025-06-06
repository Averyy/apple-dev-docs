# init(bytes:length:)

**Framework**: Foundation  
**Kind**: init

Initializes a data object filled with a given number of bytes copied from a given buffer.

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
init(bytes: UnsafeRawPointer?, length: Int)
```

#### Discussion

A data object initialized by adding to it `length` bytes of data copied from the buffer `bytes`. The returned object might be different than the original receiver.

## See Also

- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](nsdata/init(bytesnocopy:length:).md)
  Initializes a data object filled with a given number of bytes of data from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?)](nsdata/init(bytesnocopy:length:deallocator:).md)
  Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, freeWhenDone: Bool)](nsdata/init(bytesnocopy:length:freewhendone:).md)
  Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [init(data: Data)](nsdata/init(data:).md)
  Initializes a data object with the contents of another data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(bytes:length:))*