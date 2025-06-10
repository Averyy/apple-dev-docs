# Transcript.ToolCalls.Iterator

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
typealias Iterator = IndexingIterator<Transcript.ToolCalls>
```

#### Discussion

By default, a collection conforms to the `Sequence` protocol by supplying `IndexingIterator` as its associated `Iterator` type.

## See Also

- [Transcript.ToolCalls.Element](transcript/toolcalls/element.md)
  A type representing the sequence’s elements.
- [Transcript.ToolCalls.Index](transcript/toolcalls/index.md)
  A type that represents a position in the collection.
- [Transcript.ToolCalls.Indices](transcript/toolcalls/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Transcript.ToolCalls.SubSequence](transcript/toolcalls/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/iterator)*