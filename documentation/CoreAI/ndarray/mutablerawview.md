# NDArray.MutableRawView

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A type-erased mutable view over the memory owned by a tensor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct MutableRawView
```

## Topics

### Creating a mutable raw view
- [init(mutableBytes: consuming MutableRawSpan, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./mutablerawview/init%28mutablebytes,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Initialize a raw view from existing raw memory, interpreted as the specified scalar type.
- [init(metalBuffer: borrowing any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./mutablerawview/init%28metalbuffer,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Initialize a raw view from an existing metal buffer, interpreted as the specified scalar type.
- [init(ioSurface: borrowing IOSurface, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./mutablerawview/init%28iosurface,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Initialize a mutable raw view from an existing IOSurface, interpreted as the specified scalar type.
### Inspecting the view
- [var scalarType: NDArray.ScalarType](./mutablerawview/scalartype.md)
  The scalar type of the ndArray.
- [var shape: Span<Int>](./mutablerawview/shape.md)
  The shape of the ndArray.
- [var strides: Span<Int>](./mutablerawview/strides.md)
  The strides of the ndArray.
- [var mutableBytes: MutableRawSpan](./mutablerawview/mutablebytes.md)
  A mutable span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](./mutablerawview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.
### Creating typed views
- [func view<T>(as: T.Type) -> NDArray.MutableView<T>](./mutablerawview/view%28as%29.md)
  Create a typed `MutableView` of the same storage as this raw view.
### Converting to immutable
- [var rawView: NDArray.RawView](./mutablerawview/rawview.md)
  Returns an immutable raw view over the same backing data.
### Slicing the view
- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableRawView](./mutablerawview/slice%28at%29-47fbq.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.MutableRawView](./mutablerawview/slice%28at%29-82sdj.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableRawView](./mutablerawview/mutatingslice%28at%29-5tnq5.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice(at: [any NDArray.RangeExpression]) -> NDArray.MutableRawView](./mutablerawview/mutatingslice%28at%29-5ts4w.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
### Instance Methods
- [func withUnsafeMutableBytes<R, E>((UnsafeMutableRawPointer, Span<Int>, Span<Int>) throws(E) -> R) throws(E) -> R](./mutablerawview/withunsafemutablebytes%28_%29.md)
  Invokes the provided closure with the backing data and memory layout of this view.

## See Also

### Accessing views
- [NDArray.View](./view.md)
  An immutable non-owning view over the contents of a `NDArray`.
- [NDArray.MutableView](./mutableview.md)
  A mutable view over the storage of a tensor.
- [NDArray.RawView](./rawview.md)
  A type-erased immutable view over the memory owned by a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview)*