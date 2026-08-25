# ArrayLoader

**Framework**: Evaluations  
**Kind**: struct

A loader backed by an in-memory array.

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
struct ArrayLoader<Sample> where Sample : SampleProtocol
```

#### Overview

```swift
let loader = ArrayLoader(samples: [
    ModelSample(prompt: "What is 2+2?", expected: "4"),
    ModelSample(prompt: "What is the capital of France?", expected: "Paris"),
])
```

## Topics

### Initializers
- [init(samples: [Sample])](arrayloader/init(samples:).md)
  Creates a loader backed by the given array of samples.
### Instance Properties
- [var stream: any AsyncSequence<Sample, any Error>](arrayloader/stream.md)
  The async sequence that yields each sample in the array during an evaluation run.

## Relationships

### Conforms To
- [Loader](loader.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct JSONLoader](jsonloader.md)
  A loader backed by a JSON or JSONL file.
- [struct StreamLoader](streamloader.md)
  A loader backed by a custom async sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/arrayloader)*