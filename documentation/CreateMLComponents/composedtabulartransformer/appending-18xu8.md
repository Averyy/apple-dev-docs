# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with an estimator.

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
func appending<Other>(_ other: Other) -> PreprocessingEstimator<Self, Other> where Other : Estimator, Self.Output == Other.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtabulartransformer/appending(_:)-18xu8)*