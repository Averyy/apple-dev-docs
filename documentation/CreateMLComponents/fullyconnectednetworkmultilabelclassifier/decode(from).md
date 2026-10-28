# decode(from:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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

Available when `Scalar` conforms to `MLShapedArrayScalar`, `Scalar` conforms to `BinaryFloatingPoint`, `Scalar` conforms to `Decodable`, `Scalar` conforms to `Encodable`, `Label` conforms to `Comparable`, `Label` conforms to `Decodable`, `Label` conforms to `Encodable`, and `Label` conforms to `Hashable`.

## Return Value

A fully-connected network multi-label classifier model.

## Parameters

- `decoder`: A decoder for the estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/decode(from:))*