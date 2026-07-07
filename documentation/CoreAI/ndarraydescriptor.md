# NDArrayDescriptor

**Framework**: Core AI  
**Kind**: struct

A description of an array’s shape, scalar type, and memory layout expectations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NDArrayDescriptor
```

#### Overview

You obtain an `NDArrayDescriptor` from an [`InferenceFunctionDescriptor`](inferencefunctiondescriptor.md) by querying the descriptor of a specific input or output:

```swift
let valueDescriptor = functionDescriptor.inputDescriptor(of: "x")!
guard case .ndArray(let ndArrayDescriptor) = valueDescriptor else { ... }
```

The descriptor contains the expectations for an array value that you provide to an [`InferenceFunction`](inferencefunction.md). Most expectations are strict: for example, if the descriptor specifies [`scalarType`](ndarraydescriptor/scalartype.md) as `.float32`, the array you provide must use `.float32`.

## Topics

### Inspecting descriptor properties
- [var shape: [Int]](ndarraydescriptor/shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](ndarraydescriptor/scalartype.md)
  The scalar type of the array.
- [var rank: Int](ndarraydescriptor/rank.md)
  The number of dimensions in the array.
- [var hasDynamicShape: Bool](ndarraydescriptor/hasdynamicshape.md)
  A Boolean value that indicates whether the shape has any dynamic dimensions.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarraydescriptor/interleavelayout.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.
### Computing layout
- [var minimumByteCount: Int](ndarraydescriptor/minimumbytecount.md)
  The minimum number of bytes needed for storage with this descriptor’s shape and preferred strides.
- [var preferredStrides: [Int]](ndarraydescriptor/preferredstrides.md)
  The strides that avoid data layout transformations during inference.
### Resolving dynamic shapes
- [func resolvingDynamicDimensions([Int]) -> NDArrayDescriptor](ndarraydescriptor/resolvingdynamicdimensions(_:).md)
  Returns a new descriptor with all dynamic dimensions replaced by concrete values.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NDArray](ndarray.md)
  A multidimensional array of scalar values used for model inference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor)*