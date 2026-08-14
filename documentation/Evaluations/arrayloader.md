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

## Declaration

```swift
struct ArrayLoader<Sample> where Sample : SampleProtocol
```

## Topics

### Initializers
- [init(samples: [Sample])](arrayloader/init(samples:).md)
  Creates a loader backed by the given array of samples.

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