# ArrayLoader

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

A loader backed by an in-memory array.

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
struct ArrayLoader<Sample> where Sample : SampleProtocol
```

## Overview

```swift
let loader = ArrayLoader(samples: [
    ModelSample(prompt: "What is 2+2?", expected: "4"),
    ModelSample(prompt: "What is the capital of France?", expected: "Paris"),
])
```

`ArrayLoader` can also be created directly from an array literal:

```swift
let loader: ArrayLoader = [
    ModelSample(prompt: "What is 2+2?", expected: "4"),
    ModelSample(prompt: "What is the capital of France?", expected: "Paris"),
]
```

## Topics

### Initializers
- [init(arrayLiteral: Sample...)](./arrayloader/init%28arrayliteral%29.md)
  Creates a loader from an array literal of samples.
- [init(samples: [Sample])](./arrayloader/init%28samples%29.md)
  Creates a loader backed by the given array of samples.
### Instance Properties
- [var stream: any AsyncSequence<Sample, any Error>](./arrayloader/stream.md)
  The async sequence that yields each sample in the array during an evaluation run.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Loader](./loader.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Loaders
- [struct JSONLoader](./jsonloader.md)
  A loader backed by a JSON or JSONL file.
- [struct StreamLoader](./streamloader.md)
  A loader backed by a custom async sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/arrayloader)*