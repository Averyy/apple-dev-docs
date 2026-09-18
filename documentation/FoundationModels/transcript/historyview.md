# Transcript.HistoryView

**Framework**: Foundation Models  
**Kind**: struct

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
- [func append(Transcript.Entry)](transcript/historyview/append(_:).md)
  Adds an entry to the end of the history view.
- [func append(contentsOf: some Sequence<Transcript.Entry>)](transcript/historyview/append(contentsof:).md)
  Adds the entries of a sequence to the end of the history view.
### Subscripts
- [subscript(_:)](transcript/historyview/subscript(_:).md)
  Accesses the subsequence of entries within the specified bounds.
### Type Aliases
- [Transcript.HistoryView.Element](transcript/historyview/element.md)
  The type of entry the view contains.
- [Transcript.HistoryView.SubSequence](transcript/historyview/subsequence.md)
  The type that represents a contiguous subrange of the view’s entries.
### Default Implementations
- [ExpressibleByArrayLiteral Implementations](transcript/historyview/expressiblebyarrayliteral-implementations.md)
- [MutableCollection Implementations](transcript/historyview/mutablecollection-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [MutableCollection](../swift/mutablecollection.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [RangeReplaceableCollection](../swift/rangereplaceablecollection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [var history: Transcript.HistoryView](transcript/history.md)
  The transcript entries excluding the leading instructions entry, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/historyview)*