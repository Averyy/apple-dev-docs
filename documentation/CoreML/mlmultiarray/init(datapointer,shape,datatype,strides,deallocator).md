# init(dataPointer:shape:dataType:strides:deallocator:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithDataPointer:(void *) dataPointer shape:(NSArray<NSNumber *> *) shape dataType:(MLMultiArrayDataType) dataType strides:(NSArray<NSNumber *> *) strides deallocator:(void (^)(void *bytes)) deallocator error:(NSError **) error;
```

## Discussion

The caller is responsible for freeing the memory the `dataPointer` points to, by providing a `deallocator` closure.

## Parameters

- `dataPointer`: A pointer to data in memory.
- `shape`: An integer array with an element for each dimension. An element represents the size of the corresponding dimension.
- `dataType`: An [`MLMultiArrayDataType`](../mlmultiarraydatatype.md) instance that represents the pointer’s data type.
- `strides`: An integer array with an element for each dimension. An element represents the number of memory locations that span the length of the corresponding dimension.
- `deallocator`: In Swift, a closure the multiarray calls in its deinitializer. In Objective-C, a block the multiarray calls in its [`dealloc`](../../ObjectiveC/nsobject-swift.class/dealloc.md) method.

## See Also

### Creating a multiarray
- [convenience(_:)](./init%28_%29.md)
  An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](./init%28shape,datatype%29.md)
  Creates a multidimensional array with a shape and type.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](./init%28shape,datatype,strides%29.md)
  Creates the object with specified strides.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](./init%28byconcatenatingmultiarrays,alongaxis,datatype%29.md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](./init%28pixelbuffer,shape%29.md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.
- [- initWithShape:dataType:strides:](./initwithshape_datatype_strides_.md)
  Creates the object with specified strides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(datapointer:shape:datatype:strides:deallocator:))*