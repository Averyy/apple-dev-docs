# init(byConcatenatingMultiArrays:alongAxis:dataType:)

**Framework**: Core ML  
**Kind**: init

Merges an array of multiarrays into one multiarray along an axis.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(concatenating multiArrays: [MLMultiArray], axis: Int, dataType: MLMultiArrayDataType)
```

#### Discussion

All multiarray instances in `multiArrays` must have:

- The same data type
- The same number of dimensions
- The same size for each corresponding dimension, except for the concatenation axis

For example, this code concatenates two multiarrays along their first dimension:

```swift
let multiarray1 = try MLMultiArray(shape: [1, 5, 7], dataType: .int32)
let multiarray2 = try MLMultiArray(shape: [2, 5, 7], dataType: .int32)

// Merge the two multiarrays along the first dimension.
let multiArray3 = MLMultiArray(concatenating: [multiarray1, multiarray2],
                               axis: 0,
                               dataType: .int32)

assert(multiArray3.shape == [3, 5, 7])
```

## Parameters

- `multiArrays`: An   array.
- `axis`: A zero-based axis number the instances in   merge along.
- `dataType`: An   instance that represents the underlying type of all the instances in  .

## See Also

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
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](mlmultiarray/init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:))*