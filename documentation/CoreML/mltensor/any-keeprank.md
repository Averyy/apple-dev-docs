# any(keepRank:)

**Framework**: Core ML  
**Kind**: method

Computes logical OR on elements across all dimensions of a tensor where the scalar type of the tensor is expected to be Boolean.

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
func any(keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced tensor.

## Parameters

- `keepRank`: A Boolean indicating whether to keep the reduced axes or not. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/any(keeprank:))*