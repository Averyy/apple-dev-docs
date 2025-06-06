# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes the estimator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func decode(from decoder: inout any EstimatorDecoder) throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>
```

#### Return Value

A fully-connected network multi-label classifier model.

## Parameters

- `decoder`: A decoder for the estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/decode(from:))*