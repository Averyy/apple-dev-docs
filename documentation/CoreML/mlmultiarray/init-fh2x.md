# init(_:)

**Framework**: Core ML  
**Kind**: init

Creates a multiarray from a collection of floats.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Float
```

#### Discussion

Use this initializer to create a multiarray from a collection of [`Float`](https://developer.apple.com/documentation/Swift/Float) values, such as an array.

```swift
let floats: [Float] = [1.41, 1.73, 2.72, 3.14]
let floatMultiarray = try MLMultiArray(floats)
```

## Parameters

- `data`: A   of   values.

## See Also

- [convenience init<C>(C) throws](mlmultiarray/init(_:)-3eqoq.md)
  Creates a multiarray from a collection of integers.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(_:)-fh2x)*