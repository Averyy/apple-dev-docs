# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this updatable estimator with another updatable estimator.

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
func appending<Other>(_ other: Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>> where Other : UpdatableEstimator, Self.Transformer.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/appending(_:)-8ko9p)*