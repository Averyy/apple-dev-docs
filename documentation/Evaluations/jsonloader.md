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

## Declaration

```swift
struct JSONLoader<Sample> where Sample : SampleProtocol
```

#### Overview

The format is detected automatically from the file contents:

- If the first non-whitespace character is `[`, the file is treated as a JSON array (`[{...}, {...}]`) and decoded in one pass.
- Otherwise, the file is treated as JSONL (JSON Lines), where each non-empty line is decoded as an individual sample.

Malformed entries are logged via `OSLog` and skipped. A failure to open the file propagates as a thrown error.

## Topics

### Initializers
- [init(url: URL)](jsonloader/init(url:).md)
  Creates a loader backed by the JSON or JSONL file at the given URL.

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