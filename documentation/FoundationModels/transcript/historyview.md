# Transcript.HistoryView

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A mutable view into the conversational entries of a transcript.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct HistoryView
```

## Topics

### Instance Methods
- [func append(Transcript.Entry)](./historyview/append%28_%29.md)
  Adds an entry to the end of the history view.
- [func append(contentsOf: some Sequence<Transcript.Entry>)](./historyview/append%28contentsof%29.md)
  Adds the entries of a sequence to the end of the history view.
### Subscripts
- [subscript(_:)](./historyview/subscript%28_%29.md)
  Accesses the subsequence of entries within the specified bounds.
### Type Aliases
- [Transcript.HistoryView.Element](./historyview/element.md)
  The type of entry the view contains.
- [Transcript.HistoryView.SubSequence](./historyview/subsequence.md)
  The type that represents a contiguous subrange of the view’s entries.
### Default Implementations
- [ExpressibleByArrayLiteral Implementations](./historyview/expressiblebyarrayliteral-implementations.md)
- [MutableCollection Implementations](./historyview/mutablecollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [MutableCollection](../../Swift/mutablecollection.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [RangeReplaceableCollection](../../Swift/rangereplaceablecollection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Accessing the transcript history
- [var history: Transcript.HistoryView](./history.md)
  The transcript entries excluding the leading instructions entry, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/historyview)*