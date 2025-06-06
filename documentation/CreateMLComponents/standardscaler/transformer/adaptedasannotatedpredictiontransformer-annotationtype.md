# adaptedAsAnnotatedPredictionTransformer(annotationType:)

**Framework**: Create ML Components  
**Kind**: method

Returns an annotated-prediction transformer that transforms the predictions using this transformer while leaving the annotations unchanged.

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
func adaptedAsAnnotatedPredictionTransformer<Annotation>(annotationType: Annotation.Type = Annotation.self) -> some Transformer<AnnotatedPrediction<Self.Input, Annotation>, AnnotatedPrediction<Self.Output, Annotation>>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/transformer/adaptedasannotatedpredictiontransformer(annotationtype:))*