# samples

**Framework**: Evaluations  
**Kind**: property

All initial and generated samples from the most recent run.

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
var samples: [SampleType] { get }
```

#### Discussion

Before you call [`run()`](samplegenerator/run().md), this equals the samples you passed to the initializer. After iteration completes, it contains the full resulting dataset.

## See Also

- [var invalidSamples: [SampleType]](samplegenerator/invalidsamples.md)
  Samples that the validator rejected during the most recent run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/samplegenerator/samples)*