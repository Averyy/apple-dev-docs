# softmax(alongAxis:)

**Framework**: Core ML  
**Kind**: method

Computes the softmax of the specified tensor along the specified axis.

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
func softmax(alongAxis axis: Int = -1) -> MLTensor
```

#### Return Value

A new tensor with the same shape and scalar type.

## Parameters

- `axis`: The axis along which softmax will be computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/softmax(alongaxis:))*