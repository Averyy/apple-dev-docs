# init(bytesNoCopy:length:freeWhenDone:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated data object by adding the given number of bytes from the given buffer.

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
init(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int, freeWhenDone b: Bool)
```

## Parameters

- `bytes`: A buffer containing data for the new object. If   is  ,   must point to a memory block allocated with  .
- `length`: The number of bytes to hold from  . This value must not exceed the length of  .
- `b`: If  , the returned object takes ownership of the   pointer and frees it on deallocation.

## See Also

- [init(bytes: UnsafeRawPointer?, length: Int)](nsdata/init(bytes:length:).md)
  Initializes a data object filled with a given number of bytes copied from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](nsdata/init(bytesnocopy:length:).md)
  Initializes a data object filled with a given number of bytes of data from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?)](nsdata/init(bytesnocopy:length:deallocator:).md)
  Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [init(data: Data)](nsdata/init(data:).md)
  Initializes a data object with the contents of another data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(bytesnocopy:length:freewhendone:))*