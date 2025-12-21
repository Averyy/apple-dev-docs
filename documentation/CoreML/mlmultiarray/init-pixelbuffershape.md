# init(pixelBuffer:shape:)

**Framework**: Core ML  
**Kind**: init

Creates a multiarray sharing the surface of a pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])
```

#### Discussion

Use this initializer to create an [`IOSurface`](https://developer.apple.com/documentation/IOSurface)-backed `MLMultiArray` that reduces the inference latency by avoiding the buffer copy to and from some compute units.

The instance will own the pixel buffer and release it on the deallocation.

The pixel buffer’s pixel format type must be [`kCVPixelFormatType_OneComponent16Half`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent16Half). The `MLMultiArray` data type is [`MLMultiArrayDataType.float16`](mlmultiarraydatatype/float16.md).

## Parameters

- `pixelBuffer`: The pixel buffer owned by the instance.
- `shape`: The shape of the  . The last dimension of   must match the pixel buffer’s width. The product of the rest of the dimensions must match the height.

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
- [enum MLMultiArrayDataType](mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(pixelbuffer:shape:))*