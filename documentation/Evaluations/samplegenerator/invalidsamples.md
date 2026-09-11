# invalidSamples

**Framework**: Evaluations  
**Kind**: property

Samples that the validator rejected during the most recent run.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

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
  All initial and generated samples from the most recent run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/invalidsamples)*