# NDArray.MutableRawView

**Framework**: Core AI  
**Kind**: struct

A type-erased mutable view over the memory owned by a tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct MutableRawView
```

## Topics

### Creating a mutable raw view
- [init(mutableBytes: consuming MutableRawSpan, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/mutablerawview/init(mutablebytes:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a raw view from existing raw memory, interpreted as the specified scalar type.
- [init(metalBuffer: borrowing any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/mutablerawview/init(metalbuffer:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a raw view from an existing metal buffer, interpreted as the specified scalar type.
- [init(ioSurface: borrowing IOSurface, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/mutablerawview/init(iosurface:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a mutable raw view from an existing IOSurface, interpreted as the specified scalar type.
### Inspecting the view
- [var scalarType: NDArray.ScalarType](ndarray/mutablerawview/scalartype.md)
  The scalar type of the ndArray.
- [var shape: Span<Int>](ndarray/mutablerawview/shape.md)
  The shape of the ndArray.
- [var strides: Span<Int>](ndarray/mutablerawview/strides.md)
  The strides of the ndArray.
- [var mutableBytes: MutableRawSpan](ndarray/mutablerawview/mutablebytes.md)
  A mutable span over the backing bytes of this tensor.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/mutablerawview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.
### Creating typed views
- [func view<T>(as: T.Type) -> NDArray.MutableView<T>](ndarray/mutablerawview/view(as:).md)
  Create a typed `MutableView` of the same storage as this raw view.
### Converting to immutable
- [var rawView: NDArray.RawView](ndarray/mutablerawview/rawview.md)
  Returns an immutable raw view over the same backing data.
### Slicing the view
- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableRawView](ndarray/mutablerawview/slice(at:)-47fbq.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.MutableRawView](ndarray/mutablerawview/slice(at:)-82sdj.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.MutableRawView](ndarray/mutablerawview/mutatingslice(at:)-5tnq5.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func mutatingSlice(at: [any NDArray.RangeExpression]) -> NDArray.MutableRawView](ndarray/mutablerawview/mutatingslice(at:)-5ts4w.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.

## See Also

- [NDArray.View](ndarray/view.md)
  An immutable non-owning view over the contents of a `NDArray`.
- [NDArray.MutableView](ndarray/mutableview.md)
  A mutable view over the storage of a tensor.
- [NDArray.RawView](ndarray/rawview.md)
  A type-erased immutable view over the memory owned by a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview)*