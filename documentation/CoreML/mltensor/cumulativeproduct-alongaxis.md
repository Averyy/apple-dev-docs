# cumulativeProduct(alongAxis:)

**Framework**: Core ML  
**Kind**: method

Computes the cumulative product along the specified axis.

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
func cumulativeProduct(alongAxis axis: Int = 0) -> MLTensor
```

#### Return Value

The result of the cumulative product operation.

#### Discussion

The scalar type of the tensor must be numeric.

For example:

```swift
MLTensor([1, 2, 3]).cumulativeProduct() = [1, 1 * 2, 1 * 2 * 3]
```

## Parameters

- `axis`: The axis along which to perform the cumulative product. The default value is  . Must be in the range    and have a rank greater than zero.

## See Also

- [func cumulativeSum(alongAxis: Int) -> MLTensor](mltensor/cumulativesum(alongaxis:).md)
  Computes the cumulative sum along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/cumulativeproduct(alongaxis:))*