# MLShapedArray

**Framework**: Core ML  
**Kind**: struct

A machine learning collection type that stores scalar values in a multidimensional array.

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
struct MLShapedArray<Scalar> where Scalar : MLShapedArrayScalar
```

#### Overview

A shaped array is a multidimensional array type that’s the Swift counterpart to [`MLMultiArray`](mlmultiarray.md). [`MLShapedArray`](mlshapedarray.md) is one of the underlying types of `MLFeatureValue` that stores scalar values. You can convert a shaped array to an [`MLMultiArray`](mlmultiarray.md) with its [`init(_:)`](mlmultiarray/init(_:)-wk41.md) initializer, and convert back to a shaped array with its [`init(_:)`](mlshapedarray/init(_:).md) initializer. All elements in an [`MLShapedArray`](mlshapedarray.md) are of the same type, and that type must conform to [`MLShapedArrayScalar`](mlshapedarrayscalar.md):

- [`Int32`](https://developer.apple.com/documentation/Swift/Int32)
- [`Float`](https://developer.apple.com/documentation/Swift/Float)
- [`Double`](https://developer.apple.com/documentation/Swift/Double)

Each dimension in a shaped array is typically significant or meaningful. For example, a model could have an input that accepts images as a three-dimensional array of pixels, C x H x W. The first dimension, ,_ _represents the number of color channels, and the second and third dimensions,  and , represent the image’s height and width, respectively. The number of dimensions and size of each dimension define the shaped array’s .

> **Note**:  Some models use a one-dimensional multiarray for an input or output. This type of shaped array is conceptually identical to a conventional [`Array`](https://developer.apple.com/documentation/Swift/Array).

A shaped array’s [`shape`](mlmultiarray/shape.md) property is an integer array in which each element defines the size of the corresponding dimension. To inspect the shape and constraints of a model’s multiarray input or output feature:

1. Access the model’s [`modelDescription`](mlmodel/modeldescription.md) property.
2. Find the multiarray input or output feature in the model description’s [`inputDescriptionsByName`](mlmodeldescription/inputdescriptionsbyname.md) or [`outputDescriptionsByName`](mlmodeldescription/outputdescriptionsbyname.md) property, respectively.
3. Access the feature description’s [`multiArrayConstraint`](mlfeaturedescription/multiarrayconstraint.md) property.
4. Inspect the multiarray constraint’s [`shape`](mlmultiarrayconstraint/shape.md) and [`shapeConstraint`](mlmultiarrayconstraint/shapeconstraint.md).

## Topics

### Creating a shaped array
- [init(scalar: Scalar)](mlshapedarray/init(scalar:).md)
  Creates a shaped array with exactly one value and zero dimensions.
- [init<S>(scalars: S, shape: [Int])](mlshapedarray/init(scalars:shape:).md)
  Initialize with a sequence and the shape.
- [init(mutating: CVPixelBuffer, shape: [Int])](mlshapedarray/init(mutating:shape:).md)
  Creates a new `MLShapedArray` using a pixel buffer as the backing storage.
### Creating a shaped array from another type
- [init(MLMultiArray)](mlshapedarray/init(_:).md)
- [init<S>(concatenating: S, alongAxis: Int)](mlshapedarray/init(concatenating:alongaxis:).md)
  Merges a sequence of shaped arrays into one shaped array along an axis.
### Creating a shaped array with pointers to memory
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Scalar>, [Int]) throws -> Void) rethrows](mlshapedarray/init(unsafeuninitializedshape:initializingwith:).md)
  Creates a shaped array from a shape and a closure that initializes its memory.
### Creating a shaped array from data
- [init(data: Data, shape: [Int])](mlshapedarray/init(data:shape:).md)
  Creates a shaped array from a block of data and a shape.
- [init(data: Data, shape: [Int], strides: [Int])](mlshapedarray/init(data:shape:strides:).md)
  Creates a shaped array from a block of data, a shape, and strides.
### Shaping the array
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>](mlshapedarray/changinglayout(to:).md)
  Returns a copy with the specified buffer layout.
- [func expandingShape(at: Int) -> MLShapedArray<Scalar>](mlshapedarray/expandingshape(at:).md)
  Returns a new shaped array with expanded dimensions.
- [func reshaped(to: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/reshaped(to:).md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArray<Scalar>](mlshapedarray/squeezingshape.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArray<Scalar>](mlshapedarray/transposed.md)
  Returns a new transposed shaped array.
- [func transposed(permutation: [Int]) -> MLShapedArray<Scalar>](mlshapedarray/transposed(permutation:).md)
  Returns a transposed shaped array using a custom permutation.
### Reading and writing the pixel buffer
- [func withMutablePixelBufferIfAvailable<R>((CVPixelBuffer) throws -> R) rethrows -> R?](mlshapedarray/withmutablepixelbufferifavailable(_:).md)
  Writes to the underlying pixel buffer.
- [func withPixelBufferIfAvailable<R>((CVPixelBuffer) throws -> R) rethrows -> R?](mlshapedarray/withpixelbufferifavailable(_:).md)
  Reads the underlying pixel buffer.
### Modifying a shaped array
- [func withUnsafeMutableShapedBufferPointer<R>(using: MLShapedArrayBufferLayout, (inout UnsafeMutableBufferPointer<Scalar>, [Int], [Int]) throws -> R) rethrows -> R](mlshapedarray/withunsafemutableshapedbufferpointer(using:_:).md)
  Calls the given closure with a pointer to the array’s mutable storage that has a specified buffer layout.
### Encoding and decoding
- [init(from: any Decoder) throws](mlshapedarray/init(from:).md)
  Creates a shaped array from a decoder.
- [func encode(to: any Encoder) throws](mlshapedarray/encode(to:).md)
  Encode a shaped array.
### Default Implementations
- [CustomStringConvertible Implementations](mlshapedarray/customstringconvertible-implementations.md)
- [Decodable Implementations](mlshapedarray/decodable-implementations.md)
- [Encodable Implementations](mlshapedarray/encodable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
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

- [enum MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [protocol MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.
- [class MLMultiArray](mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.
- [class MLSequence](mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray)*