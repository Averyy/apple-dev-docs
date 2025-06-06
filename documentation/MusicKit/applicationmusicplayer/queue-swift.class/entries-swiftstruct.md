# ApplicationMusicPlayer.Queue.Entries

**Framework**: MusicKit  
**Kind**: struct

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Entries
```

## Topics

### Operators
- [static func == (ApplicationMusicPlayer.Queue.Entries, ApplicationMusicPlayer.Queue.Entries) -> Bool](applicationmusicplayer/queue-swift.class/entries-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init()](applicationmusicplayer/queue-swift.class/entries-swift.struct/init.md)
  Creates an empty collection of entries.
- [init(arrayLiteral: MusicPlayer.Queue.Entry...)](applicationmusicplayer/queue-swift.class/entries-swift.struct/init(arrayliteral:).md)
  Creates an instance initialized with the given elements.
### Instance Properties
- [var endIndex: ApplicationMusicPlayer.Queue.Entries.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var hashValue: Int](applicationmusicplayer/queue-swift.class/entries-swift.struct/hashvalue.md)
  The hash value.
- [var indices: ApplicationMusicPlayer.Queue.Entries.Indices](applicationmusicplayer/queue-swift.class/entries-swift.struct/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: ApplicationMusicPlayer.Queue.Entries.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: ApplicationMusicPlayer.Queue.Entries.Index, to: ApplicationMusicPlayer.Queue.Entries.Index) -> Int](applicationmusicplayer/queue-swift.class/entries-swift.struct/distance(from:to:).md)
  Returns the distance between two indices.
- [func formIndex(after: inout ApplicationMusicPlayer.Queue.Entries.Index)](applicationmusicplayer/queue-swift.class/entries-swift.struct/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout ApplicationMusicPlayer.Queue.Entries.Index)](applicationmusicplayer/queue-swift.class/entries-swift.struct/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func hash(into: inout Hasher)](applicationmusicplayer/queue-swift.class/entries-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [func index(ApplicationMusicPlayer.Queue.Entries.Index, offsetBy: Int) -> ApplicationMusicPlayer.Queue.Entries.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(ApplicationMusicPlayer.Queue.Entries.Index, offsetBy: Int, limitedBy: ApplicationMusicPlayer.Queue.Entries.Index) -> ApplicationMusicPlayer.Queue.Entries.Index?](applicationmusicplayer/queue-swift.class/entries-swift.struct/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: ApplicationMusicPlayer.Queue.Entries.Index) -> ApplicationMusicPlayer.Queue.Entries.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: ApplicationMusicPlayer.Queue.Entries.Index) -> ApplicationMusicPlayer.Queue.Entries.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/index(before:).md)
  Returns the position immediately before the given index.
- [func makeIterator() -> ApplicationMusicPlayer.Queue.Entries.Iterator](applicationmusicplayer/queue-swift.class/entries-swift.struct/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [func replaceSubrange<C>(Range<ApplicationMusicPlayer.Queue.Entries.Index>, with: C)](applicationmusicplayer/queue-swift.class/entries-swift.struct/replacesubrange(_:with:).md)
  Replaces the specified subrange of elements with the given collection.
### Subscripts
- [subscript(Range<ApplicationMusicPlayer.Queue.Entries.Index>) -> ApplicationMusicPlayer.Queue.Entries.SubSequence](applicationmusicplayer/queue-swift.class/entries-swift.struct/subscript(_:)-1doxb.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript(ApplicationMusicPlayer.Queue.Entries.Index) -> ApplicationMusicPlayer.Queue.Entries.Element](applicationmusicplayer/queue-swift.class/entries-swift.struct/subscript(_:)-6mwyn.md)
  Accesses the element at the specified position.
### Type Aliases
- [ApplicationMusicPlayer.Queue.Entries.ArrayLiteralElement](applicationmusicplayer/queue-swift.class/entries-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [ApplicationMusicPlayer.Queue.Entries.Element](applicationmusicplayer/queue-swift.class/entries-swift.struct/element.md)
  A type representing the sequence’s elements.
- [ApplicationMusicPlayer.Queue.Entries.Index](applicationmusicplayer/queue-swift.class/entries-swift.struct/index.md)
  A type that represents a position in the collection.
- [ApplicationMusicPlayer.Queue.Entries.Indices](applicationmusicplayer/queue-swift.class/entries-swift.struct/indices-swift.typealias.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [ApplicationMusicPlayer.Queue.Entries.Iterator](applicationmusicplayer/queue-swift.class/entries-swift.struct/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [ApplicationMusicPlayer.Queue.Entries.SubSequence](applicationmusicplayer/queue-swift.class/entries-swift.struct/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](applicationmusicplayer/queue-swift.class/entries-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](applicationmusicplayer/queue-swift.class/entries-swift.struct/collection-implementations.md)
- [Equatable Implementations](applicationmusicplayer/queue-swift.class/entries-swift.struct/equatable-implementations.md)
- [MutableCollection Implementations](applicationmusicplayer/queue-swift.class/entries-swift.struct/mutablecollection-implementations.md)
- [RangeReplaceableCollection Implementations](applicationmusicplayer/queue-swift.class/entries-swift.struct/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](applicationmusicplayer/queue-swift.class/entries-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [RangeReplaceableCollection](../Swift/RangeReplaceableCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct)*