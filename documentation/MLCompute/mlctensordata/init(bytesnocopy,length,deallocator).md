# init(bytesNoCopy:length:deallocator:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor data instance with a data buffer, byte length, and custom deallocator closure you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
convenience init(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int, deallocator: @escaping (UnsafeMutableRawPointer, Int) -> Void)
```

```objc
+ (instancetype) dataWithBytesNoCopy:(void *) bytes length:(NSUInteger) length deallocator:(void (^)(void *bytes, NSUInteger length)) deallocator;
```

## Return Value

A new `MLCTensorData` instance.

## Parameters

- `bytes`: A buffer that contains data.
- `length`: The number of bytes you want to reference from `bytes`. This number must not exceed the length of `bytes`.
- `deallocator`: A callback to invoke after the system deallocates the object instance.

## See Also

### Creating Tensor Data
- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](./init%28bytesnocopy,length%29.md)
  Creates a tensor data instance with the buffer of data and length of bytes you specify.
- [convenience init(immutableBytesNoCopy: UnsafeRawPointer, length: Int)](./init%28immutablebytesnocopy,length%29.md)
  Creates a tensor data instance with the buffer of immutable data and length of bytes you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata/init(bytesnocopy:length:deallocator:))*