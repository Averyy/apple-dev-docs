# encodeWithOptimizer(_:to:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Encodes the model and optimizer to an encoder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func encodeWithOptimizer(_ transformer: TimeSeriesClassifier<Scalar, Label>.Transformer, to encoder: inout any EstimatorEncoder) throws
```

Available when `Scalar` conforms to `MLShapedArrayScalar`, `Scalar` conforms to `BinaryFloatingPoint`, `Label` conforms to `Comparable`, `Label` conforms to `Decodable`, `Label` conforms to `Encodable`, and `Label` conforms to `Hashable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/encodewithoptimizer(_:to:))*