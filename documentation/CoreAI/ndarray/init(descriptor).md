# init(descriptor:)

**Framework**: Core AI  
**Kind**: init  
**Role**: Initializer

Creates an array with the shape and preferred strides from the specified descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(descriptor: consuming NDArrayDescriptor)
```

#### Discussion

The resulting array may not have a contiguous layout. The strides match the values returned by the descriptor’s preferred strides, so `contiguousElements` on a view of this array may return `nil`. In that case, use `withUnsafePointer` or `withUnsafeMutablePointer` to access the data while respecting the strides.

If the descriptor has an [`NDArray.InterleaveLayout`](./interleavelayout-swift.struct.md), the resulting ndArray will carry that interleave metadata. See [`NDArray.InterleaveLayout`](./interleavelayout-swift.struct.md) for details on how interleaved layouts affect stride semantics.

The descriptor’s [`hasDynamicShape`](../ndarraydescriptor/hasdynamicshape.md) must be `false`. If the descriptor has dynamic shapes, call [`resolvingDynamicDimensions(_:)`](../ndarraydescriptor/resolvingdynamicdimensions%28_%29.md) first.

## Parameters

- `descriptor`: The descriptor that defines the array’s shape and scalar type.

## See Also

### Creating an array
- [init(shape: [Int], scalarType: NDArray.ScalarType)](./init%28shape,scalartype%29.md)
  Creates an array with the specified shape and scalar type.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int])](./init%28shape,scalartype,strides%29.md)
  Creates an array with the specified shape, scalar type, and strides.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int], interleaveLayout: NDArray.InterleaveLayout)](./init%28shape,scalartype,strides,interleavelayout%29.md)
  Initialize an NDArray with the provided shape, scalar type, strides, and interleaved dimension.
- [init<Scalar>(scalars: some Sequence, shape: [Int])](./init%28scalars,shape%29.md)
  Initialize an ndArray with a copy of some sequence of scalars, stored in the ndArray in row-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(descriptor:))*