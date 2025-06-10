# Transcript.ToolCalls.SubSequence

**Framework**: Foundation Models  
**Kind**: typealias

A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
typealias SubSequence = Slice<Transcript.ToolCalls>
```

#### Discussion

The default subsequence type for collections that don’t define their own is `Slice`.

## See Also

- [Transcript.ToolCalls.Element](transcript/toolcalls/element.md)
  A type representing the sequence’s elements.
- [Transcript.ToolCalls.Index](transcript/toolcalls/index.md)
  A type that represents a position in the collection.
- [Transcript.ToolCalls.Indices](transcript/toolcalls/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Transcript.ToolCalls.Iterator](transcript/toolcalls/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/subsequence)*