# StreamLoader

**Framework**: Evaluations  
**Kind**: struct

A loader backed by a custom async sequence.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct StreamLoader<Sample> where Sample : SampleProtocol
```

## Topics

### Initializers
- [init(stream: some Sendable & AsyncSequence<Sample, any Error>)](streamloader/init(stream:).md)
  Creates a loader backed by the given async sequence.

## Relationships

### Conforms To
- [Loader](loader.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct ArrayLoader](arrayloader.md)
  A loader backed by an in-memory array.
- [struct JSONLoader](jsonloader.md)
  A loader backed by a JSON or JSONL file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/streamloader)*