# applied(to:)

**Framework**: Create ML Components  
**Kind**: method

Applies an augmentation per input of the base sequence.

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
func applied<S, Annotation>(to base: S) -> AugmentationSequence<S, RandomTransformer, RandomNumberGenerator, Annotation> where S : Sequence, Annotation : Equatable, S.Element == AnnotatedFeature<RandomTransformer.Input, Annotation>
```

## Mentions

- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)

#### Return Value

A sequence of augmented elements having the same number of elements as the input sequence.

## Parameters

- `base`: A sequence of elements to augment.

## See Also

- [func applied<C, Annotation>(to: C, upsampledBy: Int) -> UpsampledAugmentationSequence<C, RandomTransformer, RandomNumberGenerator, Annotation>](augmenter/applied(to:upsampledby:).md)
  Applies an augmentation repeatedly to an array of inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmenter/applied(to:))*