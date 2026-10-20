# NDArray.RawView

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A type-erased immutable view over the memory owned by a tensor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct RawView
```

## Topics

### Creating a raw view
- [init(bytes: RawSpan, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./rawview/init%28bytes,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Initialize a raw view from existing raw memory, interpreted as the specified scalar type.
- [init(metalBuffer: borrowing any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./rawview/init%28metalbuffer,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Initialize a raw view from an existing metal buffer, interpreted as the specified scalar type.
- [init(ioSurface: borrowing IOSurface, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./rawview/init%28iosurface,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Initialize a raw view from an existing IOSurface, interpreted as the specified scalar type.
### Inspecting the view
- [var scalarType: NDArray.ScalarType](./rawview/scalartype.md)
- [var shape: Span<Int>](./rawview/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](./rawview/strides.md)
  The strides of the tensor.
- [var bytes: RawSpan](./rawview/bytes.md)
  A span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./rawview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.
### Creating typed views
- [func view<T>(as: T.Type) -> NDArray.View<T>](./rawview/view%28as%29.md)
  Consume this raw view to create a typed view.
### Slicing the view
- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.RawView](./rawview/slice%28at%29-1gght.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.RawView](./rawview/slice%28at%29-kd5b.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
### Instance Methods
- [func withUnsafeBytes<R, E>((UnsafeRawPointer, Span<Int>, Span<Int>) throws(E) -> R) throws(E) -> R](./rawview/withunsafebytes%28_%29.md)
  Invokes the provided closure with the backing data and memory layout of this view.

## See Also

### Accessing views
- [NDArray.View](./view.md)
  An immutable non-owning view over the contents of a `NDArray`.
- [NDArray.MutableView](./mutableview.md)
  A mutable view over the storage of a tensor.
- [NDArray.MutableRawView](./mutablerawview.md)
  A type-erased mutable view over the memory owned by a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview)*