# MLMultiArray

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

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

```objc
@interface MLMultiArray : NSObject
```

## Mentions

- [Making Predictions with a Sequence of Inputs](./making-predictions-with-a-sequence-of-inputs.md)

#### Overview

A multidimensional array, or *multiarray*, is one of the underlying types of an `MLFeatureValue` that stores numeric values in multiple dimensions. All elements in an [`MLMultiArray`](./mlmultiarray.md) instance are one of the same type, and one of the types that [`MLMultiArrayDataType`](./mlmultiarraydatatype.md) defines:

- **[`MLMultiArrayDataType.int32`](./mlmultiarraydatatype/int32.md)**: 32-bit integer
- **[`MLMultiArrayDataType.float16`](./mlmultiarraydatatype/float16.md)**: 16-bit floating point number
- **[`MLMultiArrayDataType.float32`](./mlmultiarraydatatype/float32.md)**: 32-bit floating point number (also known as [`float`](./mlmultiarraydatatype/float.md))
- **[`float64`](./mlmultiarraydatatype/float64.md)**: 64-bit floating point number (also known as `double` in Swift or `MLMultiArrayDataTypeDouble` in Objective-C)

Each dimension in a multiarray is typically significant or meaningful. For example, a model could have an input that accepts images as a multiarray of pixels with three dimensions, C x H x W. The first dimension, *C*,_ _represents the number of color channels, and the second and third dimensions, *H* and *W*, represent the image’s height and width, respectively. The number of dimensions and size of each dimension define the multiarray’s *shape*.

> **Note**:  Some models use a one-dimensional multiarray for an input or output. This type of multiarray is conceptually identical to a conventional array.

The [`shape`](./mlmultiarray/shape.md) property is an integer array that has an element for each dimension in the multiarray. Each element in [`shape`](./mlmultiarray/shape.md) defines the size of the corresponding dimension. To inspect the shape and constraints of a model’s multiarray input or output feature:

1. Access the model’s [`modelDescription`](./mlmodel/modeldescription.md) property.
2. Find the multiarray input or output feature in the model description’s [`inputDescriptionsByName`](./mlmodeldescription/inputdescriptionsbyname.md) or [`outputDescriptionsByName`](./mlmodeldescription/outputdescriptionsbyname.md) property, respectively.
3. Access the feature description’s [`multiArrayConstraint`](./mlfeaturedescription/multiarrayconstraint.md) property.
4. Inspect the multiarray constraint’s [`shape`](./mlmultiarrayconstraint/shape.md) and [`shapeConstraint`](./mlmultiarrayconstraint/shapeconstraint.md).

## Topics

### Creating a multiarray
- [convenience(_:)](./mlmultiarray/init%28_%29.md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](./mlmultiarray/init%28shape,datatype%29.md)
  Creates a multidimensional array with a shape and type.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](./mlmultiarray/init%28shape,datatype,strides%29.md)
  Creates the object with specified strides.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](./mlmultiarray/init%28datapointer,shape,datatype,strides,deallocator%29.md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](./mlmultiarray/init%28byconcatenatingmultiarrays,alongaxis,datatype%29.md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](./mlmultiarray/init%28pixelbuffer,shape%29.md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](./mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.
- [- initWithShape:dataType:strides:](./mlmultiarray/initwithshape_datatype_strides_.md)
  Creates the object with specified strides.
### Inspecting a multiarray
- [var count: Int](./mlmultiarray/count.md)
  The total number of elements in the multiarray.
- [var dataType: MLMultiArrayDataType](./mlmultiarray/datatype.md)
  The underlying type of the multiarray.
- [var shape: [NSNumber]](./mlmultiarray/shape.md)
  The multiarray’s multidimensional shape as a number array in which each element’s value is the size of the corresponding dimension.
- [var strides: [NSNumber]](./mlmultiarray/strides.md)
  A number array in which each element is the number of memory locations that span the length of the corresponding dimension.
### Transfering the contents
- [func transfer(to: MLMultiArray)](./mlmultiarray/transfer%28to%29.md)
  Transfer the contents to the destination multi-array.
### Providing buffer access
- [func withUnsafeBufferPointer<S, R>(ofType: S.Type, (UnsafeBufferPointer<S>) throws -> R) rethrows -> R](./mlmultiarray/withunsafebufferpointer%28oftype,_%29.md)
  Calls a given closure with a raw pointer to the multiarray’s storage.
- [func withUnsafeBytes<R>((UnsafeRawBufferPointer) throws -> R) rethrows -> R](./mlmultiarray/withunsafebytes%28_%29.md)
  Calls a given closure with a raw pointer to the multiarray’s storage.
- [func withUnsafeMutableBufferPointer<S, R>(ofType: S.Type, (UnsafeMutableBufferPointer<S>, [Int]) throws -> R) rethrows -> R](./mlmultiarray/withunsafemutablebufferpointer%28oftype,_%29.md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.
- [func withUnsafeMutableBytes<R>((UnsafeMutableRawBufferPointer, [Int]) throws -> R) rethrows -> R](./mlmultiarray/withunsafemutablebytes%28_%29.md)
  Calls a given closure with a raw pointer to the multiarray’s mutable storage.
### Accessing a multiarray’s elements
- [subscript(_:)](./mlmultiarray/subscript%28_%29.md)
- [var pixelBuffer: CVPixelBuffer?](./mlmultiarray/pixelbuffer.md)
  A reference to the multiarray’s underlying pixel buffer.
- [var dataPointer: UnsafeMutableRawPointer](./mlmultiarray/datapointer.md)
  A pointer to the multiarray’s underlying memory.
- [- setObject:atIndexedSubscript:](./mlmultiarray/setobject_atindexedsubscript_.md)
  Assigns a number to the multiarray’s element at the location that the linear offset defines.
- [- setObject:forKeyedSubscript:](./mlmultiarray/setobject_forkeyedsubscript_.md)
  Assigns a number to the multiarray’s element at the location that the number array defines.
- [- getBytesWithHandler:](./mlmultiarray/getbyteswithhandler_.md)
  Get the underlying buffer pointer to read.
- [- getMutableBytesWithHandler:](./mlmultiarray/getmutablebyteswithhandler_.md)
  Get the underlying buffer pointer to mutate.
### Initializers
- [init?(coder: NSCoder)](./mlmultiarray/init%28coder%29.md)
- [convenience init(concatenating: [MLMultiArray], axis: Int, dataType: MLMultiArrayDataType)](./mlmultiarray/init%28concatenating,axis,datatype%29.md)
  Concatenate MLMultiArrays to form a new MLMultiArray.
### Default Implementations
- [MLMultiArray Implementations](./mlmultiarray/mlmultiarray-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Supporting types
- [enum MLFeatureType](./mlfeaturetype.md)
  The possible types for feature values, input features, and output features.
- [struct MLShapedArray](./mlshapedarray.md)
  A machine learning collection type that stores scalar values in a multidimensional array.
- [protocol MLShapedArrayProtocol](./mlshapedarrayprotocol.md)
  An interface that defines a shaped array type.
- [class MLSequence](./mlsequence.md)
  A machine learning collection type that stores a series of strings or integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray)*