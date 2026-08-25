# JSONLoader

**Framework**: Evaluations  
**Kind**: struct

A loader backed by a JSON or JSONL file.

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
struct JSONLoader<Sample> where Sample : SampleProtocol
```

#### Overview

```swift
let url = Bundle.main.url(forResource: "samples", withExtension: "jsonl")!
let loader = JSONLoader<ModelSample<String>>(url: url)
```

The format is detected automatically from the file contents:

- If the first non-whitespace character is `[`, the file is treated as a JSON array (`[{...}, {...}]`) and decoded in one pass.
- Otherwise, the file is treated as JSONL (JSON Lines), where the loader decodes each non-empty line as an individual sample.

Malformed entries are logged using `OSLog` and skipped. A failure to open the file propagates as a thrown error.

## Topics

### Initializers
- [init(url: URL)](jsonloader/init(url:).md)
  Creates a loader backed by the JSON or JSONL file at the given URL.
### Instance Properties
- [var stream: any AsyncSequence<Sample, any Error>](jsonloader/stream.md)
  The async sequence that reads and yields each sample from the JSON or JSONL file during an evaluation run.

## Relationships

### Conforms To
- [Loader](loader.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ArrayLoader](arrayloader.md)
  A loader backed by an in-memory array.
- [struct StreamLoader](streamloader.md)
  A loader backed by a custom async sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/jsonloader)*