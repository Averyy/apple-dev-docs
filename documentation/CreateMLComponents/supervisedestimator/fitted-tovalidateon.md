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
- watchOS 11.0+

## Declaration

```swift
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation) async throws -> Self.Transformer where Input : Sequence, Validation : Sequence, Input.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>, Validation.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>
```

## See Also

- [func adaptedAsTemporal() -> SupervisedEstimatorToTemporalAdaptor<Self>](supervisedestimator/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](supervisedestimator/fitted(to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator/fitted(to:validateon:))*