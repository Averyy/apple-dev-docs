# init(_:)

**Framework**: Core ML  
**Kind**: init

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

#### Discussion

```None
let v:[Int32] = [3, 2, 1]
let m = try MLMultiArray(v)
print(m)
Int32 3 vector
[3,2,1]
```

This initializer will trap if called with data containing FixedWidthInteger elements that cannot be safely converted to Int32, but it is safe to use with wider types so long as the actual data is within range.

```None
let a = try MLMultiArray([Int.max]) // trap!
let b = try MLMultiArray([Int(Int32.max), Int(Int32.min)]) // This is fine.
```

## See Also

- [init(shape: [NSNumber], dataType: MLMultiArrayDataType) throws](mlmultiarray/init(shape:datatype:).md)
  Creates a multidimensional array with a shape and type.
- [convenience init(shape: [Int], dataType: MLMultiArrayDataType, strides: [Int])](mlmultiarray/init(shape:datatype:strides:).md)
  Creates the object with specified strides.
- [init(dataPointer: UnsafeMutableRawPointer, shape: [NSNumber], dataType: MLMultiArrayDataType, strides: [NSNumber], deallocator: ((UnsafeMutableRawPointer) -> Void)?) throws](mlmultiarray/init(datapointer:shape:datatype:strides:deallocator:).md)
  Creates a multiarray from a data pointer.
- [convenience init(byConcatenatingMultiArrays: [MLMultiArray], alongAxis: Int, dataType: MLMultiArrayDataType)](mlmultiarray/init(byconcatenatingmultiarrays:alongaxis:datatype:).md)
  Merges an array of multiarrays into one multiarray along an axis.
- [init(pixelBuffer: CVPixelBuffer, shape: [NSNumber])](mlmultiarray/init(pixelbuffer:shape:).md)
  Creates a multiarray sharing the surface of a pixel buffer.
- [enum MLMultiArrayDataType](mlmultiarraydatatype.md)
  Constants that define the underlying element types a multiarray can store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/init(_:))*