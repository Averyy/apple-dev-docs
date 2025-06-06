# batches(ofSize:dropsLastPartialBatch:)

**Framework**: Create ML Components  
**Kind**: method

Batches a augmentation sequence.

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
func batches(ofSize size: Int, dropsLastPartialBatch: Bool) -> AugmentationSequence<Base, RandomTransformer, RandomNumberGenerator, Annotation>.BatchedSequence
```

#### Return Value

An async sequence of batches.

## Parameters

- `size`: The number of elements contained in each batch.
- `dropsLastPartialBatch`: A Boolean value representing whether the last batch should be dropped if it has less   than   elements.

## See Also

- [AugmentationSequence.BatchedSequence](augmentationsequence/batchedsequence.md)
  An async sequence that batches an augmentation sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/batches(ofsize:dropslastpartialbatch:))*