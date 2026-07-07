# invalidSamples

**Framework**: Evaluations  
**Kind**: property

Samples that the validator rejected during the most recent run.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var invalidSamples: [SampleType] { get }
```

## Mentions

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)

#### Discussion

Returns an empty array when no validator was provided.

## See Also

- [var samples: [SampleType]](samplegenerator/samples.md)
  All samples — initial and generated — from the most recent run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/invalidsamples)*