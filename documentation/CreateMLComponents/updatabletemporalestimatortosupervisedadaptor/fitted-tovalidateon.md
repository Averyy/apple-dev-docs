# fitted(to:validateOn:)

**Framework**: Create ML Components  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fitted<InputSequence, Validation, FeatureSequence>(to input: InputSequence, validateOn validation: Validation) async throws -> Self.Transformer where InputSequence : Sequence, Validation : Sequence, FeatureSequence : TemporalSequence, InputSequence.Element == AnnotatedFeature<FeatureSequence, Self.Annotation>, Validation.Element == AnnotatedFeature<FeatureSequence, Self.Annotation>, FeatureSequence.Feature == Self.Transformer.Input
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor/fitted(to:validateon:))*