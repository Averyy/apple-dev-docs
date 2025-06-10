# MLShapedArraySlice

**Framework**: Core ML  
**Kind**: struct

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

### Creating a Shaped Array Slice
- [init(scalar: Scalar)](mlshapedarrayslice/init(scalar:).md)
  Creates a shaped array slice with exactly one value and zero dimensions.
- [init<S>(scalars: S, shape: [Int])](mlshapedarrayslice/init(scalars:shape:).md)
  Initialize with a sequence and the shape.
### Creating a Shaped Array Slice from Another Type
- [init(MLMultiArray)](mlshapedarrayslice/init(_:).md)
  Creates a new MLShapedArraySlice using a `MLMultiArray` as a backing storage.
- [init<S>(concatenating: S, alongAxis: Int)](mlshapedarrayslice/init(concatenating:alongaxis:).md)
  Merges a sequence of shaped arrays into one shaped array along an axis.
### Creating a Shaped Array Slice with Pointers to Memory
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Scalar>, [Int]) throws -> Void) rethrows](mlshapedarrayslice/init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array slice from a shape and a closure that initializes its memory.
### Creating a Shaped Array Slice with Data
- [init(data: Data, shape: [Int])](mlshapedarrayslice/init(data:shape:).md)
  Creates a shaped array with a defined data and shape.
- [init(data: Data, shape: [Int], strides: [Int])](mlshapedarrayslice/init(data:shape:strides:).md)
  Creates a shaped array with defined data, shape, and strides.
### Encoding and Decoding an Array Slice
- [init(from: any Decoder) throws](mlshapedarrayslice/init(from:).md)
  Creates an array slice from the passed decoder.
- [func encode(to: any Encoder) throws](mlshapedarrayslice/encode(to:).md)
  Encodes the array slice.
### Supporting Types
- [Shaped Array Slice Collection Operations](shaped-array-slice-collection-operations.md)
  Properties and methods a shaped array slice inherits from collection protocols.
### Initializers
- [init(mutating: CVPixelBuffer, shape: [Int])](mlshapedarrayslice/init(mutating:shape:).md)
  Creates a new `MLShapedArraySlice` using a pixel buffer as the backing storage.
### Instance Methods
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArraySlice<Scalar>](mlshapedarrayslice/changinglayout(to:).md)
  Returns a copy with the specified buffer layout.
- [func expandingShape(at: Int) -> MLShapedArraySlice<Scalar>](mlshapedarrayslice/expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions
- [func reshaped(to: [Int]) -> MLShapedArraySlice<Scalar>](mlshapedarrayslice/reshaped(to:).md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArraySlice<Scalar>](mlshapedarrayslice/squeezingshape.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArraySlice<Scalar>](mlshapedarrayslice/transposed.md)
  Returns a new transposed shaped array
- [func transposed(permutation: [Int]) -> MLShapedArraySlice<Scalar>](mlshapedarrayslice/transposed(permutation:).md)
  Returns a new transposed shaped array using a custom permutation.
- [func withUnsafeMutableShapedBufferPointer<R>(using: MLShapedArrayBufferLayout, (inout UnsafeMutableBufferPointer<Scalar>, [Int], [Int]) throws -> R) rethrows -> R](mlshapedarrayslice/withunsafemutableshapedbufferpointer(using:_:).md)
  Calls the given closure with a pointer to the array’s mutable storage that has a specified buffer layout.
### Default Implementations
- [Decodable Implementations](mlshapedarrayslice/decodable-implementations.md)
- [Encodable Implementations](mlshapedarrayslice/encodable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [MLShapedArrayProtocol](mlshapedarrayprotocol.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [associatedtype Scalar : MLShapedArrayScalar](mlshapedarrayprotocol/scalar-swift.associatedtype.md)
  Represents the underlying scalar type of the shaped array type.
- [protocol MLShapedArrayScalar](mlshapedarrayscalar.md)
  A type that associates a scalar with a shaped array.
- [protocol MLShapedArrayRangeExpression](mlshapedarrayrangeexpression.md)
  An interface for a range expression, which you typically use with subscripts of shaped array types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayslice)*