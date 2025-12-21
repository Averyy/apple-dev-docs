# init(shape:dataType:strides:)

**Framework**: Core ML  
**Kind**: init

Creates the object with specified strides.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])
```

#### Discussion

The contents of the object are left uninitialized; the client must initialize it.

## Parameters

- `shape`: The shape
- `dataType`: The data type
- `strides`: The strides.

## See Also

- [convenience(_:)](mlmultiarray/init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](mlmultiarray/init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](mlmultiarray/init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](mlmultiarray/init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(shape:datatype:strides:))*