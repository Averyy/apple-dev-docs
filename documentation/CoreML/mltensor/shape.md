# shape

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The shape of the tensor.

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
var shape: [Int] { get }
```

## Discussion

For example, 2 x 3 matrix may be represented as a tensor with the shape of `[2, 3]`.

## See Also

### Accessing tensor properties
- [var isScalar: Bool](./isscalar.md)
  A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.
- [var rank: Int](./rank.md)
  The number of dimensions of the tensor.
- [var scalarCount: Int](./scalarcount.md)
  The number of scalar elements in the tensor.
- [var scalarType: any MLTensorScalar.Type](./scalartype.md)
  The type of scalars in the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/shape)*