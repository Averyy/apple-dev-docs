# sampling

**Framework**: Foundation Models  
**Kind**: property

A sampling strategy for how the model picks tokens when generating a response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var sampling: GenerationOptions.SamplingMode?
```

#### Discussion

When you execute a prompt on a model, the model produces a probability for every token in its vocabulary. The sampling strategy controls how the model narrows down the list of tokens to consider during that process. A strategy that picks the single most likely token yields a predictable response every time, but other strategies offer results that often sound more natural to a person.

> **Note**: Leaving the `sampling` nil lets the system choose a a reasonable default on your behalf.

## See Also

- [GenerationOptions.SamplingMode](generationoptions/samplingmode.md)
  A type that defines how values are sampled from a probability distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/sampling)*