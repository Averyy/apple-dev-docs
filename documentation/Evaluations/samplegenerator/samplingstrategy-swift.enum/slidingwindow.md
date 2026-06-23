# SampleGenerator.SamplingStrategy.slidingWindow

**Framework**: Evaluations  
**Kind**: case

A strategy that slides a window through the examples, advancing it each batch.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case slidingWindow
```

## Mentions

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)

#### Discussion

When the model repeats an inference, this strategy continues retrying as long as there are new windows of examples to show the model.

## See Also

- [SampleGenerator.SamplingStrategy.random(retries:)](samplegenerator/samplingstrategy-swift.enum/random(retries:).md)
  A strategy that randomly picks a subset of samples each time a model repeats inference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/samplingstrategy-swift.enum/slidingwindow)*