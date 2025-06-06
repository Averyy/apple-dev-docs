# decodeWithOptimizer(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes a previously fitted transformer with an optimizer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func decodeWithOptimizer(from decoder: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifier<Scalar, Label>.Transformer
```

#### Return Value

A fully connected network classifier model.

## Parameters

- `decoder`: A decoder for the estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/decodewithoptimizer(from:))*