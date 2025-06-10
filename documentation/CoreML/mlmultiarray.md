# MLMultiArray

**Framework**: Core ML  
**Kind**: class

A machine learning collection type that stores numeric values in an array with multiple dimensions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class MLMultiArray
```

## Mentions

- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)

#### Overview

A multidimensional array, or , is one of the underlying types of an `MLFeatureValue` that stores numeric values in multiple dimensions. All elements in an [`MLMultiArray`](mlmultiarray.md) instance are one of the same type, and one of the types that [`MLMultiArrayDataType`](mlmultiarraydatatype.md) defines:

Each dimension in a multiarray is typically significant or meaningful. For example, a model could have an input that accepts images as a multiarray of pixels with three dimensions, C x H x W. The first dimension, ,_ _represents the number of color channels, and the second and third dimensions,  and , represent the image’s height and width, respectively. The number of dimensions and size of each dimension define the multiarray’s .

> **Note**:  Some models use a one-dimensional multiarray for an input or output. This type of multiarray is conceptually identical to a conventional array.

The [`shape`](mlmultiarray/shape.md) property is an integer array that has an element for each dimension in the multiarray. Each element in [`shape`](mlmultiarray/shape.md) defines the size of the corresponding dimension. To inspect the shape and constraints of a model’s multiarray input or output feature:

1. Access the model’s [`modelDescription`](mlmodel/modeldescription.md) property.
2. Find the multiarray input or output feature in the model description’s [`inputDescriptionsByName`](mlmodeldescription/inputdescriptionsbyname.md) or [`outputDescriptionsByName`](mlmodeldescription/outputdescriptionsbyname.md) property, respectively.
3. Access the feature description’s [`multiArrayConstraint`](mlfeaturedescription/multiarrayconstraint.md) property.
4. Inspect the multiarray constraint’s [`shape`](mlmultiarrayconstraint/shape.md) and [`shapeConstraint`](mlmultiarrayconstraint/shapeconstraint.md).

## Topics

### Creating a Multiarray
- [convenience init<C>(C) throws](mlmultiarray/init(_:)-3eqoq.md)
  Creates a multiarray from a collection of integers.
- [convenience init<C>(C) throws](mlmultiarray/init(_:)-fh2x.md)
  Creates a multiarray from a collection of floats.
- [convenience init<C>(C) throws](mlmultiarray/init(_:)-8bsfu.md)
  Creates a multiarray from a collection of doubles.
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](mlmultiarray/init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.
- [convenience init<ShapedArray>(ShapedArray)](mlmultiarray/init(_:)-wk41.md)
  Creates a multiarray from a shaped array.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](mlmultiarray/init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](mlmultiarray/init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.
### Inspecting a Multiarray
- [var count: Int](mlmultiarray/count.md)
  The total number of elements in the multiarray.
- [var dataType: MLMultiArrayDataType](mlmultiarray/datatype.md)
  The underlying type of the multiarray.
- [var shape: [NSNumber]](mlmultiarray/shape.md)
  The multiarray’s multidimensional shape as a number array in which each element’s value is the size of the corresponding dimension.
- [var strides: [NSNumber]](mlmultiarray/strides.md)
  A number array in which each element is the number of memory locations that span the length of the corresponding dimension.
### Providing buffer access
- [func withUnsafeBufferPointer<S, R>(ofType: S.Type, (UnsafeBufferPointer<S>) throws -> R) rethrows -> R](mlmultiarray/withunsafebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](mlmultiarray/withunsafebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s storage.
- [func withUnsafeMutableBufferPointer<S, R>(ofType: S.Type, (UnsafeMutableBufferPointer<S>, [Int]) throws -> R) rethrows -> R](mlmultiarray/withunsafemutablebufferpointer(oftype:_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer, [Int]) throws -> R) rethrows -> R](mlmultiarray/withunsafemutablebytes(_:).md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.
### Accessing a Multiarray’s Elements
- [subscript(Int) -> NSNumber](mlmultiarray/subscript(_:)-2hh91.md)
  Accesses the multiarray by using a linear offset.
- [subscript([NSNumber]) -> NSNumber](mlmultiarray/subscript(_:)-3d9el.md)
  Accesses the multiarray by using a number array that has an element for each dimension.
- [var pixelBuffer: CVPixelBuffer?](mlmultiarray/pixelbuffer.md)
  A reference to the multiarray’s underlying pixel buffer.
- [var dataPointer: UnsafeMutableRawPointer](mlmultiarray/datapointer.md)
  A pointer to the multiarray’s underlying memory.
### Initializers
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](mlmultiarray/init(shape:datatype:strides:).md)
  Creates the object with specified strides.
### Instance Methods
- [func transfer(to: MLMultiArray)](mlmultiarray/transfer(to:).md)
  Transfer the contents to the destination multi-array.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [enum MLFeatureType](mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [struct MLShapedArray](mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.
- [protocol MLShapedArrayProtocol](mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.
- [class MLSequence](mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray)*