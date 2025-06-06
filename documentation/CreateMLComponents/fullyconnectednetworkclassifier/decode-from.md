# decode(from:)

**Framework**: Create ML Components  
**Kind**: method

Decodes the estimator.

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
func decode(from decoder: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifierModel<Scalar, Label>
```

#### Return Value

A fully connected network classifier model.

## Parameters

- `decoder`: A decoder for the estimator.

## See Also

- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkclassifier/encode(_:to:).md)
  Encodes a fitted encodable transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/decode(from:))*