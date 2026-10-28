# init(bytesNoCopy:length:deallocator:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithBytesNoCopy:(void *) bytes length:(NSUInteger) length deallocator:(void (^)(void *bytes, NSUInteger length)) deallocator;
```

## Return Value

A data object initialized by adding to it `length` bytes of data from the buffer `bytes`. The returned object might be different than the original receiver.

## Discussion

Use this method to define your own deallocation behavior for the data buffer you provide.

In order to avoid any inadvertent strong reference cycles, you should avoid capturing pointers to any objects that may in turn maintain strong references to the `NSData` object. This includes explicit references to `self`, and implicit references to `self` due to direct instance variable access. To make it easier to avoid these references, the `deallocator` block takes two parameters, a pointer to the `buffer`, and its length; you should always use these values instead of trying to use references from outside the block.

## Parameters

- `bytes`: A buffer containing data for the new object.
- `length`: The number of bytes to hold from `bytes`. This value must not exceed the length of `bytes`.
- `deallocator`: A block to invoke when the resulting `NSData` object is deallocated.

## See Also

### Creating Data
- [init(bytes: UnsafeRawPointer?, length: Int)](./init%28bytes,length%29.md)
  Initializes a data object filled with a given number of bytes copied from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](./init%28bytesnocopy,length%29.md)
  Initializes a data object filled with a given number of bytes of data from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, freeWhenDone: Bool)](./init%28bytesnocopy,length,freewhendone%29.md)
  Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [init(data: Data)](./init%28data%29.md)
  Initializes a data object with the contents of another data object.
- [+ data](./data.md)
  Creates an empty data object.
- [+ dataWithBytes:length:](./datawithbytes_length_.md)
  Creates a data object containing a given number of bytes copied from a given buffer.
- [+ dataWithBytesNoCopy:length:](./datawithbytesnocopy_length_.md)
  Creates a data object that holds a given number of bytes from a given buffer.
- [+ dataWithBytesNoCopy:length:freeWhenDone:](./datawithbytesnocopy_length_freewhendone_.md)
  Creates a data object that holds a given number of bytes from a given buffer.
- [+ dataWithData:](./datawithdata_.md)
  Creates a data object containing the contents of another data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(bytesnocopy:length:deallocator:))*