# init(shape:dataType:)

**Framework**: Core ML  
**Kind**: init

Creates a multidimensional array with a shape and type.

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
init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws
```

#### Discussion

This method allocates a contiguous region of memory for the multiarray’s shape. You must set the contents of memory. The multiarray frees the memory in its deinitializer (Swift) or [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) method (Objective-C).

The following code creates a 3 x 3 multiarray and sets its contents to the value 3.14159.

## Parameters

- `shape`: An integer array that has an element for each dimension in a multiarray that represents its length.
- `dataType`: An element type defined by  .

## See Also

- [convenience init<C>(C) throws](mlmultiarray/init(_:)-3eqoq.md)
  Creates a multiarray from a collection of integers.
- [convenience init<C>(C) throws](mlmultiarray/init(_:)-fh2x.md)
  Creates a multiarray from a collection of floats.
- [convenience init<C>(C) throws](mlmultiarray/init(_:)-8bsfu.md)
  Creates a multiarray from a collection of doubles.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(shape:datatype:))*