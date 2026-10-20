# MLShapedArray

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

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

A shaped array is a multidimensional array type that’s the Swift counterpart to [`MLMultiArray`](./mlmultiarray.md). [`MLShapedArray`](./mlshapedarray.md) is one of the underlying types of `MLFeatureValue` that stores scalar values. You can convert a shaped array to an [`MLMultiArray`](./mlmultiarray.md) with its [`init(_:)`](./mlmultiarray/init%28_%29-wk41.md) initializer, and convert back to a shaped array with its [`init(_:)`](./mlshapedarray/init%28_%29.md) initializer. All elements in an [`MLShapedArray`](./mlshapedarray.md) are of the same type, and that type must conform to [`MLShapedArrayScalar`](./mlshapedarrayscalar.md):

- [`Int32`](../Swift/int32.md)
- [`Float`](../Swift/float.md)
- [`Double`](../Swift/double.md)

Each dimension in a shaped array is typically significant or meaningful. For example, a model could have an input that accepts images as a three-dimensional array of pixels, C x H x W. The first dimension, *C*,_ _represents the number of color channels, and the second and third dimensions, *H* and *W*, represent the image’s height and width, respectively. The number of dimensions and size of each dimension define the shaped array’s *shape*.

> **Note**:  Some models use a one-dimensional multiarray for an input or output. This type of shaped array is conceptually identical to a conventional [`Array`](../Swift/array.md).

A shaped array’s [`shape`](./mlmultiarray/shape.md) property is an integer array in which each element defines the size of the corresponding dimension. To inspect the shape and constraints of a model’s multiarray input or output feature:

1. Access the model’s [`modelDescription`](./mlmodel/modeldescription.md) property.
2. Find the multiarray input or output feature in the model description’s [`inputDescriptionsByName`](./mlmodeldescription/inputdescriptionsbyname.md) or [`outputDescriptionsByName`](./mlmodeldescription/outputdescriptionsbyname.md) property, respectively.
3. Access the feature description’s [`multiArrayConstraint`](./mlfeaturedescription/multiarrayconstraint.md) property.
4. Inspect the multiarray constraint’s [`shape`](./mlmultiarrayconstraint/shape.md) and [`shapeConstraint`](./mlmultiarrayconstraint/shapeconstraint.md).

## Topics

### Creating a shaped array
- [init(scalar: Scalar)](./mlshapedarray/init%28scalar%29.md)
  Creates a shaped array with exactly one value and zero dimensions.
- [init<S>(scalars: S, shape: [Int])](./mlshapedarray/init%28scalars,shape%29.md)
  Initialize with a sequence and the shape.
- [init(mutating: CVPixelBuffer, shape: [Int])](./mlshapedarray/init%28mutating,shape%29.md)
  Creates a new `MLShapedArray` using a pixel buffer as the backing storage.
### Creating a shaped array from another type
- [init(MLMultiArray)](./mlshapedarray/init%28_%29.md)
- [init<S>(concatenating: S, alongAxis: Int)](./mlshapedarray/init%28concatenating,alongaxis%29.md)
  Merges a sequence of shaped arrays into one shaped array along an axis.
### Creating a shaped array with pointers to memory
- [init(unsafeUninitializedShape: [Int], initializingWith: (inout UnsafeMutableBufferPointer<Scalar>, [Int]) throws -> Void) rethrows](./mlshapedarray/init%28unsafeuninitializedshape,initializingwith%29.md)
  Creates a shaped array from a shape and a closure that initializes its memory.
### Creating a shaped array from data
- [init(data: Data, shape: [Int])](./mlshapedarray/init%28data,shape%29.md)
  Creates a shaped array from a block of data and a shape.
- [init(data: Data, shape: [Int], strides: [Int])](./mlshapedarray/init%28data,shape,strides%29.md)
  Creates a shaped array from a block of data, a shape, and strides.
### Shaping the array
- [func changingLayout(to: MLShapedArrayBufferLayout) -> MLShapedArray<Scalar>](./mlshapedarray/changinglayout%28to%29.md)
  Returns a copy with the specified buffer layout.
- [func expandingShape(at: Int) -> MLShapedArray<Scalar>](./mlshapedarray/expandingshape%28at%29.md)
  Returns a new shaped array with expanded dimensions.
- [func reshaped(to: [Int]) -> MLShapedArray<Scalar>](./mlshapedarray/reshaped%28to%29.md)
  Returns a new reshaped shaped array.
- [func squeezingShape() -> MLShapedArray<Scalar>](./mlshapedarray/squeezingshape%28%29.md)
  Returns a new squeezed shaped array.
- [func transposed() -> MLShapedArray<Scalar>](./mlshapedarray/transposed%28%29.md)
  Returns a new transposed shaped array.
- [func transposed(permutation: [Int]) -> MLShapedArray<Scalar>](./mlshapedarray/transposed%28permutation%29.md)
  Returns a transposed shaped array using a custom permutation.
### Reading and writing the pixel buffer
- [func withMutablePixelBufferIfAvailable<R>((CVPixelBuffer) throws -> R) rethrows -> R?](./mlshapedarray/withmutablepixelbufferifavailable%28_%29.md)
  Writes to the underlying pixel buffer.
- [func withPixelBufferIfAvailable<R>((CVPixelBuffer) throws -> R) rethrows -> R?](./mlshapedarray/withpixelbufferifavailable%28_%29.md)
  Reads the underlying pixel buffer.
### Modifying a shaped array
- [func withUnsafeMutableShapedBufferPointer<R>(using: MLShapedArrayBufferLayout, (inout UnsafeMutableBufferPointer<Scalar>, [Int], [Int]) throws -> R) rethrows -> R](./mlshapedarray/withunsafemutableshapedbufferpointer%28using,_%29.md)
  Calls the given closure with a pointer to the array’s mutable storage that has a specified buffer layout.
### Encoding and decoding
- [init(from: any Decoder) throws](./mlshapedarray/init%28from%29.md)
  Creates a shaped array from a decoder.
- [func encode(to: any Encoder) throws](./mlshapedarray/encode%28to%29.md)
  Encode a shaped array.
### Default Implementations
- [CustomStringConvertible Implementations](./mlshapedarray/customstringconvertible-implementations.md)
- [Decodable Implementations](./mlshapedarray/decodable-implementations.md)
- [Encodable Implementations](./mlshapedarray/encodable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
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
- [enum MLFeatureType](./mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [protocol MLShapedArrayProtocol](./mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.
- [class MLMultiArray](./mlmultiarray.md)
  A machine learning collection type that stores numeric values in an array with multiple dimensions.
- [class MLSequence](./mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarray)*