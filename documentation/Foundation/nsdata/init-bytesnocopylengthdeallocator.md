# init(bytesNoCopy:length:deallocator:)

**Framework**: Foundation  
**Kind**: init

Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.

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
init(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)? = nil)
```

#### Return Value

A data object initialized by adding to it `length` bytes of data from the buffer `bytes`. The returned object might be different than the original receiver.

#### Discussion

Use this method to define your own deallocation behavior for the data buffer you provide.

In order to avoid any inadvertent strong reference cycles, you should avoid capturing pointers to any objects that may in turn maintain strong references to the `NSData` object. This includes explicit references to `self`, and implicit references to `self` due to direct instance variable access. To make it easier to avoid these references, the `deallocator` block takes two parameters, a pointer to the `buffer`, and its length; you should always use these values instead of trying to use references from outside the block.

## Parameters

- `bytes`: A buffer containing data for the new object.
- `length`: The number of bytes to hold from  . This value must not exceed the length of  .
- `deallocator`: A block to invoke when the resulting   object is deallocated.

## See Also

- [init(bytes: UnsafeRawPointer?, length: Int)](nsdata/init(bytes:length:).md)
  Initializes a data object filled with a given number of bytes copied from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](nsdata/init(bytesnocopy:length:).md)
  Initializes a data object filled with a given number of bytes of data from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, freeWhenDone: Bool)](nsdata/init(bytesnocopy:length:freewhendone:).md)
  Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [init(data: Data)](nsdata/init(data:).md)
  Initializes a data object with the contents of another data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(bytesnocopy:length:deallocator:))*