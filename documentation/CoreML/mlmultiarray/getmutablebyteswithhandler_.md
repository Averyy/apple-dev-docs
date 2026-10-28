# getMutableBytesWithHandler:

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Get the underlying buffer pointer to mutate.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```objc
- (void) getMutableBytesWithHandler:(void (^)(void *mutableBytes, NSInteger size, NSArray<NSNumber *> *strides)) handler;
```

## Discussion

The buffer contains a collection of `int32`, `float16`, `float32`, or `float64` values, depending on the multiarray’s data type. It may not store these scalar values contiguously; use `strides` to get the buffer layout.

## Parameters

- `handler`: The block to receive the buffer pointer, its size in bytes, and strides. This block has no return value and takes the following parameters:

  - **bytes**: The pointer to the buffer.
  - **size**: The size of the buffer.
  - **strides**: The strides of the buffer in scalars. Note that this may be different from `strides`’s value prior to this method invocation.

## See Also

### Accessing a multiarray’s elements
- [- setObject:atIndexedSubscript:](./setobject_atindexedsubscript_.md)
  Assigns a number to the multiarray’s element at the location that the linear offset defines.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Assigns a number to the multiarray’s element at the location that the number array defines.
- [- getBytesWithHandler:](./getbyteswithhandler_.md)
  Get the underlying buffer pointer to read.
- [var pixelBuffer: CVPixelBuffer?](./pixelbuffer.md)
  A reference to the multiarray’s underlying pixel buffer.
- [var dataPointer: UnsafeMutableRawPointer](./datapointer.md)
  A pointer to the multiarray’s underlying memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/getmutablebyteswithhandler:)*