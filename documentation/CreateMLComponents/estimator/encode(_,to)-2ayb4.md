# encode(_:to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Encodes a fitted encodable transformer.

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
func encode(_ transformer: Self.Transformer, to encoder: inout any EstimatorEncoder) throws
```

Available when `Transformer` conforms to `Encodable`.

## Parameters

- `transformer`: A transformer created by this estimator.
- `encoder`: An estimator encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/encode(_:to:)-2ayb4)*