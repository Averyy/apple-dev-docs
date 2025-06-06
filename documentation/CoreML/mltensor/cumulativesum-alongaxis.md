# cumulativeSum(alongAxis:)

**Framework**: Core ML  
**Kind**: method

Computes the cumulative sum along the specified axis.

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
func cumulativeSum(alongAxis axis: Int = 0) -> MLTensor
```

#### Return Value

The result of the cumulative sum operation.

#### Discussion

The scalar type of the tensor must be numeric.

For example:

```swift
MLTensor([1, 2, 3]).cumulativeSum() = [1, 1 + 2, 1 + 2 + 3]
```

## Parameters

- `axis`: The axis along which to perform the cumulative sum. The default value is  . Must be in the range    and have a rank greater than zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/cumulativesum(alongaxis:))*