# appending(_:)

**Framework**: Create ML Components  
**Kind**: method

Composes this transformer with a prediction-only transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func appending<Other, Annotation>(_ other: Other) -> some Transformer<Self.Input, AnnotatedPrediction<Other.Output, Annotation>> where Other : Transformer, Self.Output == AnnotatedPrediction<Other.Input, Annotation>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagereader/appending(_:)-fxm8)*