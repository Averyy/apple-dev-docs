# Transcript.Iterator

**Framework**: Foundation Models  
**Kind**: typealias

A type that provides the collection’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
typealias Iterator = IndexingIterator<Transcript>
```

#### Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/iterator)*