# BidirectionalCollection

**Framework**: Swift  
**Kind**: protocol

A collection that supports backward as well as forward traversal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol BidirectionalCollection<Element> : Collection where Self.Indices : BidirectionalCollection, Self.SubSequence : BidirectionalCollection
```

#### Overview

Bidirectional collections offer traversal backward from any valid index, not including a collection’s `startIndex`. Bidirectional collections can therefore offer additional operations, such as a `last` property that provides efficient access to the last element and a `reversed()` method that presents the elements in reverse order. In addition, bidirectional collections have more efficient implementations of some sequence and collection methods, such as `suffix(_:)`.

### Conforming to the Bidirectionalcollection Protocol

To add `BidirectionalProtocol` conformance to your custom types, implement the `index(before:)` method in addition to the requirements of the `Collection` protocol.

Indices that are moved forward and backward in a bidirectional collection move by the same amount in each direction. That is, for any valid index `i` into a bidirectional collection `c`:

- If `i >= c.startIndex && i < c.endIndex`, then `c.index(before: c.index(after: i)) == i`.
- If `i > c.startIndex && i <= c.endIndex`, then `c.index(after: c.index(before: i)) == i`.

Valid indices are exactly those indices that are reachable from the collection’s `startIndex` by repeated applications of `index(after:)`, up to, and including, the `endIndex`.

## Topics

### Associated Types
- [associatedtype Element](bidirectionalcollection/element.md)
  A type representing the sequence’s elements.
- [associatedtype Index](bidirectionalcollection/index.md)
  A type that represents a position in the collection.
- [associatedtype Indices](bidirectionalcollection/indices-swift.associatedtype.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [associatedtype SubSequence](bidirectionalcollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Instance Properties
- [var endIndex: Self.Index](bidirectionalcollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Self.Indices](bidirectionalcollection/indices-4qv42.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var last: Self.Element?](bidirectionalcollection/last.md)
  The last element of the collection.
- [var startIndex: Self.Index](bidirectionalcollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func contains(some RegexComponent) -> Bool](bidirectionalcollection/contains(_:)-1l08t.md)
  Returns a Boolean value indicating whether the collection contains the given regex.
- [func contains(() -> some RegexComponent) -> Bool](bidirectionalcollection/contains(_:)-60wyq.md)
  Returns a Boolean value indicating whether this collection contains a match for the regex, where the regex is created by the given closure.
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](bidirectionalcollection/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](bidirectionalcollection/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
- [func distance(from: Self.Index, to: Self.Index) -> Int](bidirectionalcollection/distance(from:to:).md)
  Returns the distance between two indices.
- [func dropLast(Int) -> Self.SubSequence](bidirectionalcollection/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func firstMatch<Output>(of: () -> some RegexComponent) -> Regex<Output>.Match?](bidirectionalcollection/firstmatch(of:)-6v8ci.md)
  Returns the first match for the regex within this collection, where the regex is created by the given closure.
- [func firstMatch<Output>(of: some RegexComponent) -> Regex<Output>.Match?](bidirectionalcollection/firstmatch(of:)-7m8f4.md)
  Returns the first match of the specified regex within the collection.
- [func firstRange(of: some RegexComponent) -> Range<Self.Index>?](bidirectionalcollection/firstrange(of:)-1di7b.md)
  Finds and returns the range of the first occurrence of a given regex within the collection.
- [func firstRange(of: () -> some RegexComponent) -> Range<Self.Index>?](bidirectionalcollection/firstrange(of:)-3jqrg.md)
  Returns the range of the first match for the regex within this collection, where the regex is created by the given closure.
- [func firstRange<C>(of: C) -> Range<Self.Index>?](bidirectionalcollection/firstrange(of:)-5sum7.md)
  Finds and returns the range of the first occurrence of a given collection within this collection.
- [func formIndex(after: inout Self.Index)](bidirectionalcollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Self.Index)](bidirectionalcollection/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](bidirectionalcollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](bidirectionalcollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Self.Index) -> Self.Index](bidirectionalcollection/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Self.Index) -> Self.Index](bidirectionalcollection/index(before:).md)
  Returns the position immediately before the given index.
- [func joined(separator: String) -> String](bidirectionalcollection/joined(separator:).md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](bidirectionalcollection/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](bidirectionalcollection/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](bidirectionalcollection/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func matches<Output>(of: () -> some RegexComponent) -> [Regex<Output>.Match]](bidirectionalcollection/matches(of:)-5eey9.md)
  Returns a collection containing all non-overlapping matches of the regex, created by the given closure.
- [func matches<Output>(of: some RegexComponent) -> [Regex<Output>.Match]](bidirectionalcollection/matches(of:)-5hhx.md)
  Returns a collection containing all matches of the specified regex.
- [func popLast() -> Self.Element?](bidirectionalcollection/poplast.md)
  Removes and returns the last element of the collection.
- [func prefixMatch<Output>(of: () -> some RegexComponent) -> Regex<Output>.Match?](bidirectionalcollection/prefixmatch(of:)-2fwv6.md)
  Matches part of the regex, starting at the beginning, where the regex is created by the given closure.
- [func prefixMatch<R>(of: R) -> Regex<R.RegexOutput>.Match?](bidirectionalcollection/prefixmatch(of:)-7dq6v.md)
  Returns a match if this string is matched by the given regex at its start.
- [func ranges(of: some RegexComponent) -> [Range<Self.Index>]](bidirectionalcollection/ranges(of:)-40wx3.md)
  Finds and returns the ranges of the all occurrences of a given sequence within the collection.
- [func ranges(of: () -> some RegexComponent) -> [Range<Self.Index>]](bidirectionalcollection/ranges(of:)-9qfdo.md)
  Returns the ranges of the all non-overlapping matches for the regex within this collection, where the regex is created by the given closure.
- [func removeLast() -> Self.Element](bidirectionalcollection/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](bidirectionalcollection/removelast(_:).md)
  Removes the given number of elements from the end of the collection.
- [func reversed() -> ReversedCollection<Self>](bidirectionalcollection/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, separator: () -> some RegexComponent) -> [Self.SubSequence]](bidirectionalcollection/split(maxsplits:omittingemptysubsequences:separator:).md)
  Returns the longest possible subsequences of the collection, in order, around subsequence that match the regex created by the given closure.
- [func split(separator: some RegexComponent, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](bidirectionalcollection/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given separator.
- [func starts(with: some RegexComponent) -> Bool](bidirectionalcollection/starts(with:)-4972u.md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in the specified regex.
- [func starts(with: () -> some RegexComponent) -> Bool](bidirectionalcollection/starts(with:)-97xlm.md)
  Returns a Boolean value indicating whether the initial elements of this collection are a match for the regex created by the given closure.
- [func suffix(Int) -> Self.SubSequence](bidirectionalcollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func trimmingPrefix(some RegexComponent) -> Self.SubSequence](bidirectionalcollection/trimmingprefix(_:)-1luge.md)
  Returns a new collection of the same type by removing the initial elements that matches the given regex.
- [func trimmingPrefix(() -> some RegexComponent) -> Self.SubSequence](bidirectionalcollection/trimmingprefix(_:)-781ik.md)
  Returns a subsequence of this collection by removing the elements matching the regex from the start, where the regex is created by the given closure.
- [func wholeMatch<Output>(of: () -> some RegexComponent) -> Regex<Output>.Match?](bidirectionalcollection/wholematch(of:)-1wbp6.md)
  Matches a regex in its entirety, where the regex is created by the given closure.
- [func wholeMatch<R>(of: R) -> Regex<R.RegexOutput>.Match?](bidirectionalcollection/wholematch(of:)-7741n.md)
  Returns a match if this string is matched by the given regex in its entirety.
### Subscripts
- [subscript(Self.Index) -> Self.Element](bidirectionalcollection/subscript(_:)-5tj5.md)
  Accesses the element at the specified position.
- [subscript(Range<Self.Index>) -> Self.SubSequence](bidirectionalcollection/subscript(_:)-7tzd8.md)
  Accesses a contiguous subrange of the collection’s elements.

## Relationships

### Inherits From
- [Collection](collection.md)
- [Sequence](sequence.md)
### Inherited By
- [RandomAccessCollection](randomaccesscollection.md)
- [StringProtocol](stringprotocol.md)
### Conforming Types
- [AnyBidirectionalCollection](anybidirectionalcollection.md)
- [AnyRandomAccessCollection](anyrandomaccesscollection.md)
- [AnyRegexOutput](anyregexoutput.md)
- [Array](array.md)
- [ArraySlice](arrayslice.md)
- [ClosedRange](closedrange.md)
- [CollectionOfOne](collectionofone.md)
- [ContiguousArray](contiguousarray.md)
- [DefaultIndices](defaultindices.md)
- [DiscontiguousSlice](discontiguousslice.md)
- [EmptyCollection](emptycollection.md)
- [EnumeratedSequence](enumeratedsequence.md)
- [FlattenSequence](flattensequence.md)
- [Int.Words](int/words-swift.struct.md)
- [Int16.Words](int16/words-swift.struct.md)
- [Int32.Words](int32/words-swift.struct.md)
- [Int64.Words](int64/words-swift.struct.md)
- [Int8.Words](int8/words-swift.struct.md)
- [KeyValuePairs](keyvaluepairs.md)
- [LazyDropWhileSequence](lazydropwhilesequence.md)
- [LazyFilterSequence](lazyfiltersequence.md)
- [LazyMapSequence](lazymapsequence.md)
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md)
- [LazySequence](lazysequence.md)
- [Range](range.md)
- [RangeSet.Ranges](rangeset/ranges-swift.struct.md)
- [Repeated](repeated.md)
- [ReversedCollection](reversedcollection.md)
- [Slice](slice.md)
- [String](string.md)
- [String.UTF16View](string/utf16view.md)
- [String.UTF8View](string/utf8view.md)
- [String.UnicodeScalarView](string/unicodescalarview.md)
- [Substring](substring.md)
- [Substring.UTF16View](substring/utf16view.md)
- [Substring.UTF8View](substring/utf8view.md)
- [Substring.UnicodeScalarView](substring/unicodescalarview.md)
- [UInt.Words](uint/words-swift.struct.md)
- [UInt128.Words](uint128/words-swift.struct.md)
- [UInt16.Words](uint16/words-swift.struct.md)
- [UInt32.Words](uint32/words-swift.struct.md)
- [UInt64.Words](uint64/words-swift.struct.md)
- [UInt8.Words](uint8/words-swift.struct.md)
- [Unicode.Scalar.UTF16View](unicode/scalar/utf16view.md)
- [Unicode.Scalar.UTF8View](unicode/scalar/utf8view.md)
- [UnsafeBufferPointer](unsafebufferpointer.md)
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md)
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md)

## See Also

- [protocol RandomAccessCollection](randomaccesscollection.md)
  A collection that supports efficient random-access index traversal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection)*