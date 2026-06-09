# samples

**Framework**: Evaluations  
**Kind**: property

All samples — initial and generated — from the most recent run.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var samples: [SampleType] { get }
```

#### Discussion

Before [`run()`](samplegenerator/run().md) is called, this equals `initialSamples`. After iteration completes, it contains the full resulting dataset.

## See Also

- [var invalidSamples: [SampleType]](samplegenerator/invalidsamples.md)
  Samples that the validator rejected during the most recent run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/samples)*