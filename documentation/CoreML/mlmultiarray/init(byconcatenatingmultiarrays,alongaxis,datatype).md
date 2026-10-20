# init(byConcatenatingMultiArrays:alongAxis:dataType:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

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
convenience init(byConcatenatingMultiArrays multiArrays: [MLMultiArray], alongAxis axis: Int, dataType: MLMultiArrayDataType)
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

- `multiArrays`: An [`MLMultiArray`](../mlmultiarray.md) array.
- `axis`: A zero-based axis number the instances in `multiArray` merge along.
- `dataType`: An [`MLMultiArrayDataType`](../mlmultiarraydatatype.md) instance that represents the underlying type of all the instances in `multiArrays`.

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
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](./init%28pixelbuffer,shape%29.md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:))*