# MLMultiArrayDataType

**Framework**: Core ML  
**Kind**: enum

Constants that define the underlying element types a multiarray can store.

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
enum MLMultiArrayDataType
```

#### Overview

All elements of an [`MLMultiArray`](mlmultiarray.md) instance must be of the same type and must be defined in [`MLMultiArrayDataType`](mlmultiarraydatatype.md).

## Topics

### Multiarray data types
- [MLMultiArrayDataType.int8](mlmultiarraydatatype/int8.md)
- [MLMultiArrayDataType.int32](mlmultiarraydatatype/int32.md)
  Designates the multiarray’s elements as 32-bit integers.
- [MLMultiArrayDataType.float16](mlmultiarraydatatype/float16.md)
  Designates the multiarray’s elements as 16-bit floats.
- [MLMultiArrayDataType.float32](mlmultiarraydatatype/float32.md)
  Designates the multiarray’s elements as 32-bit floats.
- [MLMultiArrayDataType.double](mlmultiarraydatatype/double.md)
  Designates the multiarray’s elements as doubles.
- [static var float: MLMultiArrayDataType](mlmultiarraydatatype/float.md)
  Designates the multiarray’s elements as floats.
- [static var float64: MLMultiArrayDataType](mlmultiarraydatatype/float64.md)
  Designates the multiarray’s elements as 64-bit floats.
### Creating a multiarray data type
- [init?(rawValue: Int)](mlmultiarraydatatype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience(_:)](mlmultiarray/init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](mlmultiarray/init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](mlmultiarray/init(shape:datatype:strides:).md)
  Creates the object with specified strides.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](mlmultiarray/init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](mlmultiarray/init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarraydatatype)*