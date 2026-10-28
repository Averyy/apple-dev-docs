# init(immutableBytesNoCopy:length:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor data instance with the buffer of immutable data and length of bytes you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(immutableBytesNoCopy bytes: UnsafeRawPointer, length: Int)
```

```objc
+ (instancetype) dataWithImmutableBytesNoCopy:(const void *) bytes length:(NSUInteger) length;
```

## Discussion

> ❗ **Important**:  Don’t mutate the underlying bytes in a tensor data instance you create with this initializer. Doing so may result in unexpected behavior.

## Parameters

- `bytes`: A buffer that contains immutable data.
- `length`: The number of bytes you choose to reference from `bytes`. This number must not exceed the length of `bytes`.

## See Also

### Creating Tensor Data
- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](./init%28bytesnocopy,length%29.md)
  Creates a tensor data instance with the buffer of data and length of bytes you specify.
- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: (UnsafeMutableRawPointer, Int) -> Void)](./init%28bytesnocopy,length,deallocator%29.md)
  Creates a tensor data instance with a data buffer, byte length, and custom deallocator closure you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata/init(immutablebytesnocopy:length:))*