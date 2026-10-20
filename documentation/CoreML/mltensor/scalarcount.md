# scalarCount

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The number of scalar elements in the tensor.

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
var scalarCount: Int { get }
```

## See Also

### Accessing tensor properties
- [var isScalar: Bool](./isscalar.md)
  A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.
- [var rank: Int](./rank.md)
  The number of dimensions of the tensor.
- [var scalarType: any MLTensorScalar.Type](./scalartype.md)
  The type of scalars in the tensor.
- [var shape: [Int]](./shape.md)
  The shape of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/scalarcount)*