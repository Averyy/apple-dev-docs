# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this updatable estimator with a transformer.

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
func appending<Other>(_ other: Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation> where Other : Transformer, Other.Input == Self.Transformer.Output
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/appending(_:)-47t7f)*