# init(pixelBuffer:shape:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithPixelBuffer:(CVPixelBufferRef) pixelBuffer shape:(NSArray<NSNumber *> *) shape;
```

#### Discussion

Use this initializer to create an [IOSurface](../../IOSurface/IOSurface.md)-backed `MLMultiArray` that reduces the inference latency by avoiding the buffer copy to and from some compute units.

The instance will own the pixel buffer and release it on the deallocation.

The pixel buffer’s pixel format type must be [`kCVPixelFormatType_OneComponent16Half`](../../CoreVideo/kcvpixelformattype_onecomponent16half.md). The `MLMultiArray` data type is [`MLMultiArrayDataType.float16`](../mlmultiarraydatatype/float16.md).

## Parameters

- `pixelBuffer`: The pixel buffer owned by the instance.
- `shape`: The shape of the `MLMultiArray`. The last dimension of `shape` must match the pixel buffer’s width. The product of the rest of the dimensions must match the height.

## See Also

### Creating a multiarray
- [convenience(_:)](./init%28_%29.md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](./init%28shape,datatype%29.md)
  Creates a multidimensional array with a shape and type.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](./init%28shape,datatype,strides%29.md)
  Creates the object with specified strides.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](./init%28datapointer,shape,datatype,strides,deallocator%29.md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](./init%28byconcatenatingmultiarrays,alongaxis,datatype%29.md)
  Merges an array of multiarrays into one multiarray along an axis.
- [enum MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(pixelbuffer:shape:))*