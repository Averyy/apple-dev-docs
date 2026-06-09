# NDArray.RawView

**Framework**: Core AI  
**Kind**: struct

A type-erased immutable view over the memory owned by a tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RawView
```

## Topics

### Inspecting the view
- [var scalarType: NDArray.ScalarType](ndarray/rawview/scalartype.md)
- [var shape: Span<Int>](ndarray/rawview/shape.md)
  The shape of the tensor.
- [var strides: Span<Int>](ndarray/rawview/strides.md)
  The strides of the tensor.
- [var bytes: RawSpan](ndarray/rawview/bytes.md)
  A span over the backing bytes of this tensor.
### Creating typed views
- [func view<T>(as: T.Type) -> NDArray.View<T>](ndarray/rawview/view(as:).md)
  Consume this raw view to create a typed view.
### Initializers
- [init(bytes: RawSpan, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/rawview/init(bytes:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a raw view from existing raw memory, interpreted as the specified scalar type.
- [init(ioSurface: borrowing IOSurface, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/rawview/init(iosurface:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a raw view from an existing IOSurface, interpreted as the specified scalar type.
- [init(metalBuffer: borrowing any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/rawview/init(metalbuffer:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a raw view from an existing metal buffer, interpreted as the specified scalar type.
### Instance Properties
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/rawview/interleavelayout.md)
  Returns which dimension is interleaved, and by what factor it is interleaved. Or returns `nil` if there is not an interleaved dimension.
### Instance Methods
- [func slice<let indexRank : Int>(at: [indexRank of any NDArray.RangeExpression]) -> NDArray.RawView](ndarray/rawview/slice(at:)-1gght.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.
- [func slice(at: [any NDArray.RangeExpression]) -> NDArray.RawView](ndarray/rawview/slice(at:)-kd5b.md)
  Returns a sub-view with the same rank as this view by slicing the dimensions at the provided ranges.

## See Also

- [NDArray.View](ndarray/view.md)
  An immutable non-owning view over the contents of a `NDArray`.
- [NDArray.MutableView](ndarray/mutableview.md)
  A mutable view over the storage of a tensor.
- [NDArray.MutableRawView](ndarray/mutablerawview.md)
  A type-erased mutable view over the memory owned by a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview)*