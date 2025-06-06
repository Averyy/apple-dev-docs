# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to an async sequence of examples while validating with a validation sequence.

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
func fitted<Input, Validation>(to input: Input, validateOn validation: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer where Input : AsyncSequence, Validation : Sequence, Input.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>, Validation.Element == AnnotatedFeature<Self.Transformer.Input, Self.Annotation>
```

#### Return Value

The fitted transformer.

#### Discussion

Note that the async sequence is collected before fitting the estimator. This may result in increased memory use. Consider using the update method to train progressively in batches.

## Parameters

- `input`: An async sequence of examples used for fitting the transformer.
- `validation`: A sequence of examples used for validating the fitted transformer.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/fitted(to:validateon:eventhandler:)-7hp54)*