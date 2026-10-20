# MLShapedArraySlice

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

A multidimensional subset of elements from a shaped array type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct MLShapedArraySlice<Scalar> where Scalar : MLShapedArrayScalar
```

## Topics

### Creating a shaped array slice
- [init(scalar: Scalar)](./mlshapedarrayslice/init%28scalar%29.md)
  Creates a shaped array slice with exactly one value and zero dimensions.
- [init<S>(scalars: S, shape: [Int])](./mlshapedarrayslice/init%28scalars,shape%29.md)
  Initialize with a sequence and the shape.
- [init(mutating: CVPixelBuffer, shape: [Int])](./mlshapedarrayslice/init%28mutating,shape%29.md)
  Creates a new `MLShapedArraySlice` using a pixel buffer as the backing storage.
### Creating a shaped array slice from another type
- [init(MLMultiArray)](./mlshapedarrayslice/init%28_%29.md)
  Creates a new MLShapedArraySlice using a `MLMultiArray` as a backing storage.
- [init<S>(concatenating: S, alongAxis: Int)](./mlshapedarrayslice/init%28concatenating,alongaxis%29.md)
  Merges a sequence of shaped arrays into one shaped array along an axis.
### Creating a shaped array slice with pointers to memory
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Scalar>, [Int]) throws -> Void) rethrows](./mlshapedarrayslice/init%28unsafeuninitializedshape,initializingwith%29.md)
  Creates a shaped array slice from a shape and a closure that initializes its memory.
### Creating a shaped array slice with data
- [init(data: Data, shape: [Int])](./mlshapedarrayslice/init%28data,shape%29.md)
  Creates a shaped array with a defined data and shape.
- [init(data: Data, shape: [Int], strides: [Int])](./mlshapedarrayslice/init%28data,shape,strides%29.md)
  Creates a shaped array with defined data, shape, and strides.
### Shaping the array slice
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArraySlice<Scalar>](./mlshapedarrayslice/changinglayout%28to%29.md)
  Returns a copy with the specified buffer layout.
- [func expandingShape(at: Int) -> MLShapedArraySlice<Scalar>](./mlshapedarrayslice/expandingshape%28at%29.md)
  Returns a new shaped array with expanded dimensions
- [func reshaped(to: [Int]) -> MLShapedArraySlice<Scalar>](./mlshapedarrayslice/reshaped%28to%29.md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArraySlice<Scalar>](./mlshapedarrayslice/squeezingshape%28%29.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArraySlice<Scalar>](./mlshapedarrayslice/transposed%28%29.md)
  Returns a new transposed shaped array
- [func transposed(permutation: [Int]) -> MLShapedArraySlice<Scalar>](./mlshapedarrayslice/transposed%28permutation%29.md)
  Returns a new transposed shaped array using a custom permutation.
### Modifying a shaped array type
- [func withUnsafeMutableShapedBufferPointer<R>(using: MLShapedArrayBufferLayout, (inout UnsafeMutableBufferPointer<Scalar>, [Int], [Int]) throws -> R) rethrows -> R](./mlshapedarrayslice/withunsafemutableshapedbufferpointer%28using,_%29.md)
  Calls the given closure with a pointer to the array’s mutable storage that has a specified buffer layout.
### Encoding and decoding an array slice
- [init(from: any Decoder) throws](./mlshapedarrayslice/init%28from%29.md)
  Creates an array slice from the passed decoder.
- [func encode(to: any Encoder) throws](./mlshapedarrayslice/encode%28to%29.md)
  Encodes the array slice.
### Default Implementations
- [Decodable Implementations](./mlshapedarrayslice/decodable-implementations.md)
- [Encodable Implementations](./mlshapedarrayslice/encodable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [MLShapedArrayProtocol](./mlshapedarrayprotocol.md)
- [MutableCollection](../Swift/mutablecollection.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Supporting types
- [associatedtype Scalar : MLShapedArrayScalar](./mlshapedarrayprotocol/scalar-swift.associatedtype.md)
  Represents the underlying scalar type of the shaped array type.
- [protocol MLShapedArrayScalar](./mlshapedarrayscalar.md)
  A type that associates a scalar with a shaped array.
- [protocol MLShapedArrayRangeExpression](./mlshapedarrayrangeexpression.md)
  An interface for a range expression, which you typically use with subscripts of shaped array types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice)*