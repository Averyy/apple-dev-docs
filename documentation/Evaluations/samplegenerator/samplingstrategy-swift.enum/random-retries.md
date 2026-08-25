# SampleGenerator.SamplingStrategy.random(retries:)

**Framework**: Evaluations  
**Kind**: case

A strategy that randomly picks a subset of samples each time a model repeats inference.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
case random(retries: Int = 5)
```

## Mentions

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)

#### Discussion

When the model repeats an inference, this strategy retries up to `retries` times, selecting a random subset to steer the model toward a new inference.

## Parameters

- `retries`: The maximum number of retries when the model repeats an inference.

## See Also

- [SampleGenerator.SamplingStrategy.slidingWindow](samplegenerator/samplingstrategy-swift.enum/slidingwindow.md)
  A strategy that slides a window through the examples, advancing it each batch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/samplingstrategy-swift.enum/random(retries:))*