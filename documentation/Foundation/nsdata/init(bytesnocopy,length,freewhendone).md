# init(bytesNoCopy:length:freeWhenDone:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithBytesNoCopy:(void *) bytes length:(NSUInteger) length freeWhenDone:(BOOL) b;
```

## Parameters

- `bytes`: A buffer containing data for the new object. If `flag` is [`true`](../../Swift/true.md), `bytes` must point to a memory block allocated with `malloc`.
- `length`: The number of bytes to hold from `bytes`. This value must not exceed the length of `bytes`.
- `b`: If [`true`](../../Swift/true.md), the returned object takes ownership of the `bytes` pointer and frees it on deallocation.

## See Also

### Creating Data
- [init(bytes: UnsafeRawPointer?, length: Int)](./init%28bytes,length%29.md)
  Initializes a data object filled with a given number of bytes copied from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](./init%28bytesnocopy,length%29.md)
  Initializes a data object filled with a given number of bytes of data from a given buffer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?)](./init%28bytesnocopy,length,deallocator%29.md)
  Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [init(data: Data)](./init%28data%29.md)
  Initializes a data object with the contents of another data object.
- [+ data](./data.md)
  Creates an empty data object.
- [+ dataWithBytes:length:](./datawithbytes_length_.md)
  Creates a data object containing a given number of bytes copied from a given buffer.
- [+ dataWithBytesNoCopy:length:](./datawithbytesnocopy_length_.md)
  Creates a data object that holds a given number of bytes from a given buffer.
- [+ dataWithData:](./datawithdata_.md)
  Creates a data object containing the contents of another data object.
### Related Documentation
- [+ dataWithBytesNoCopy:length:freeWhenDone:](./datawithbytesnocopy_length_freewhendone_.md)
  Creates a data object that holds a given number of bytes from a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(bytesnocopy:length:freewhendone:))*