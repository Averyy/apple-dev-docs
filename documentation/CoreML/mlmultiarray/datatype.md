# dataType

**Framework**: Core ML  
**Kind**: property

The underlying type of the multiarray.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var dataType: MLMultiArrayDataType { get }
```

## See Also

- [var count: Int](mlmultiarray/count.md)
  The total number of elements in the multiarray.
- [var shape: [NSNumber]](mlmultiarray/shape.md)
  The multiarray’s multidimensional shape as a number array in which each element’s value is the size of the corresponding dimension.
- [var strides: [NSNumber]](mlmultiarray/strides.md)
  A number array in which each element is the number of memory locations that span the length of the corresponding dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/datatype)*