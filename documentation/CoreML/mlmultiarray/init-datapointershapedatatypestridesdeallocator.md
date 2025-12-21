# init(dataPointer:shape:dataType:strides:deallocator:)

**Framework**: Core ML  
**Kind**: init

Creates a multiarray from a data pointer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)? = nil) throws
```

#### Discussion

The caller is responsible for freeing the memory the `dataPointer` points to, by providing a `deallocator` closure.

## Parameters

- `dataPointer`: A pointer to data in memory.
- `shape`: An integer array with an element for each dimension. An element represents the size of the corresponding dimension.
- `dataType`: An   instance that represents the pointer’s data type.
- `strides`: An integer array with an element for each dimension. An element represents the number of memory locations that span the length of the corresponding dimension.
- `deallocator`: In Swift, a closure the multiarray calls in its deinitializer. In Objective-C, a block the multiarray calls in its   method.

## See Also

- [convenience(_:)](mlmultiarray/init(_:).md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](mlmultiarray/init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](mlmultiarray/init(shape:datatype:strides:).md)
  Creates the object with specified strides.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](mlmultiarray/init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(datapointer:shape:datatype:strides:deallocator:))*