# init(_:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

An MLMultiArray constructed with the FixedWidthInteger elements of the collection converted to Int32.

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
convenience init<C>(_ data: C) throws where C : Collection, C.Element : FixedWidthInteger
```

**Other overloads**:

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Double
```

```swift
convenience init<C>(_ data: C) throws where C : Collection, C.Element == Float
```

```swift
convenience init<ShapedArray>(_ shapedArray: ShapedArray) where ShapedArray : MLShapedArrayProtocol
```

## Discussion

```
let v:[Int32] = [3, 2, 1]
let m = try MLMultiArray(v)
print(m)
Int32 3 vector
[3,2,1]
```

This initializer will trap if called with data containing FixedWidthInteger elements that cannot be safely converted to Int32, but it is safe to use with wider types so long as the actual data is within range.

```
let a = try MLMultiArray([Int.max]) // trap!
let b = try MLMultiArray([Int(Int32.max), Int(Int32.min)]) // This is fine.
```

## See Also

### Creating a multiarray
- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](./init%28shape,datatype%29.md)
  Creates a multidimensional array with a shape and type.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](./init%28shape,datatype,strides%29.md)
  Creates the object with specified strides.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](./init%28datapointer,shape,datatype,strides,deallocator%29.md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](./init%28byconcatenatingmultiarrays,alongaxis,datatype%29.md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](./init%28pixelbuffer,shape%29.md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](../mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(_:))*