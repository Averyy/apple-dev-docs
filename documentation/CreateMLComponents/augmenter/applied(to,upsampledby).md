# applied(to:upsampledBy:)

**Framework**: Create ML Components  
**Kind**: method

Applies an augmentation repeatedly to an array of inputs.

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
func applied<C, Annotation>(to elements: C, upsampledBy count: Int) -> UpsampledAugmentationSequence<C, RandomTransformer, RandomNumberGenerator, Annotation> where C : Collection, Annotation : Equatable, C.Element == AnnotatedFeature<RandomTransformer.Input, Annotation>
```

## Mentions

- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)

#### Return Value

A sequence of augmented elements having `count` times the number of elements in the input collection.

## Parameters

- `elements`: A collection of elements to augment.
- `count`: The number of times to shuffle and augment the input elements. Must be at least one.

## See Also

- [func applied<S, Annotation>(to: S) -> AugmentationSequence<S, RandomTransformer, RandomNumberGenerator, Annotation>](augmenter/applied(to:).md)
  Applies an augmentation per input of the base sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmenter/applied(to:upsampledby:))*