# NDArray

**Framework**: Core AI  
**Kind**: struct

A multidimensional array of scalar values used for model inference.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct NDArray
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Overview

An `NDArray` stores data in a layout defined by its [`shape`](ndarray/shape.md), [`scalarType`](ndarray/scalartype-swift.property.md), and [`strides`](ndarray/strides.md).

## Topics

### Creating an array
- [init(shape: [Int], scalarType: NDArray.ScalarType)](ndarray/init(shape:scalartype:).md)
  Creates an array with the specified shape and scalar type.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int])](ndarray/init(shape:scalartype:strides:).md)
  Creates an array with the specified shape, scalar type, and strides.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int], interleaveLayout: NDArray.InterleaveLayout)](ndarray/init(shape:scalartype:strides:interleavelayout:).md)
  Initialize an NDArray with the provided shape, scalar type, strides, and interleaved dimension.
- [init<Scalar>(scalars: some Sequence, shape: [Int])](ndarray/init(scalars:shape:).md)
  Initialize an ndArray with a copy of some sequence of scalars, stored in the ndArray in row-major order.
- [init(descriptor: consuming NDArrayDescriptor)](ndarray/init(descriptor:).md)
  Creates an array with the shape and preferred strides from the specified descriptor.
### Inspecting an array
- [var shape: [Int]](ndarray/shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](ndarray/scalartype-swift.property.md)
  The scalar type of the array.
- [var strides: [Int]](ndarray/strides.md)
  The distance, in elements, between consecutive values along each dimension.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/interleavelayout-swift.property.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.
### Accessing elements
- [func view<T>(as: T.Type) -> NDArray.View<T>](ndarray/view(as:).md)
  Returns a read-only, typed view of this array’s elements.
- [func mutableView<T>(as: T.Type) -> NDArray.MutableView<T>](ndarray/mutableview(as:).md)
  Returns a mutable, typed view of this array’s elements.
- [func rawView() -> NDArray.RawView](ndarray/rawview.md)
  Returns a read-only, raw view of this array’s storage.
- [func mutableRawView() -> NDArray.MutableRawView](ndarray/mutablerawview.md)
  Returns a mutable, raw view of this array’s storage.
### Accessing views
- [NDArray.View](ndarray/view.md)
  An immutable non-owning view over the contents of a `NDArray`.
- [NDArray.MutableView](ndarray/mutableview.md)
  A mutable view over the storage of a tensor.
- [NDArray.RawView](ndarray/rawview.md)
  A type-erased immutable view over the memory owned by a tensor.
- [NDArray.MutableRawView](ndarray/mutablerawview.md)
  A type-erased mutable view over the memory owned by a tensor.
### Defining scalar types
- [NDArray.ScalarType](ndarray/scalartype-swift.enum.md)
  The possible scalar types.
### Describing interleaved layouts
- [NDArray.InterleaveLayout](ndarray/interleavelayout-swift.struct.md)
  Describes the interleaved memory layout of an ndArray dimension.
### Supporting subscripts
- [protocol RangeExpression](ndarray/rangeexpression.md)

## Relationships

### Conforms To
- [Escapable](../swift/escapable.md)
- [InferenceValue.MutableViewRepresentable](inferencevalue/mutableviewrepresentable.md)
- [InferenceValue.ViewRepresentable](inferencevalue/viewrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct NDArrayDescriptor](ndarraydescriptor.md)
  A description of an array’s shape, scalar type, and memory layout expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray)*