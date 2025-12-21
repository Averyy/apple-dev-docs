# isScalar

**Framework**: Core ML  
**Kind**: property

A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var isScalar: Bool { get }
```

## See Also

- [var rank: Int](mltensor/rank.md)
  The number of dimensions of the tensor.
- [var scalarCount: Int](mltensor/scalarcount.md)
  The number of scalar elements in the tensor.
- [var scalarType: any MLTensorScalar.Type](mltensor/scalartype.md)
  The type of scalars in the tensor.
- [var shape: [Int]](mltensor/shape.md)
  The shape of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/isscalar)*