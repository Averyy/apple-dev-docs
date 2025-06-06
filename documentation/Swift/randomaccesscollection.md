# RandomAccessCollection

**Framework**: Swift  
**Kind**: protocol

A collection that supports efficient random-access index traversal.

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
protocol RandomAccessCollection<Element> : BidirectionalCollection where Self.Indices : RandomAccessCollection, Self.SubSequence : RandomAccessCollection
```

#### Overview

Random-access collections can move indices any distance and measure the distance between indices in O(1) time. Therefore, the fundamental difference between random-access and bidirectional collections is that operations that depend on index movement or distance measurement offer significantly improved efficiency. For example, a random-access collection’s `count` property is calculated in O(1) instead of requiring iteration of an entire collection.

### Conforming to the Randomaccesscollection Protocol

The `RandomAccessCollection` protocol adds further constraints on the associated `Indices` and `SubSequence` types, but otherwise imposes no additional requirements over the `BidirectionalCollection` protocol. However, in order to meet the complexity guarantees of a random-access collection, either the index for your custom type must conform to the `Strideable` protocol or you must implement the `index(_:offsetBy:)` and `distance(from:to:)` methods with O(1) efficiency.

## Topics

### Associated Types
- [associatedtype Element](randomaccesscollection/element.md)
  A type representing the sequence’s elements.
- [associatedtype Index](randomaccesscollection/index.md)
  A type that represents a position in the collection.
- [associatedtype Indices](randomaccesscollection/indices-swift.associatedtype.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [associatedtype SubSequence](randomaccesscollection/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Instance Properties
- [var endIndex: Self.Index](randomaccesscollection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Self.Indices](randomaccesscollection/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Self.Index](randomaccesscollection/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](randomaccesscollection/distance(from:to:).md)
  Returns the distance between two indices.
- [func formIndex(after: inout Self.Index)](randomaccesscollection/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Self.Index)](randomaccesscollection/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Self.Index, offsetBy: Int) -> Self.Index](randomaccesscollection/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](randomaccesscollection/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Self.Index) -> Self.Index](randomaccesscollection/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Self.Index) -> Self.Index](randomaccesscollection/index(before:).md)
  Returns the position immediately before the given index.
### Subscripts
- [subscript(Self.Index) -> Self.Element](randomaccesscollection/subscript(_:)-2mluu.md)
  Accesses the element at the specified position.
- [subscript(Range<Self.Index>) -> Self.SubSequence](randomaccesscollection/subscript(_:)-3fc50.md)
  Accesses a contiguous subrange of the collection’s elements.

## Relationships

### Inherits From
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [Sequence](sequence.md)
### Conforming Types
- [AnyRandomAccessCollection](anyrandomaccesscollection.md)
- [AnyRegexOutput](anyregexoutput.md)
- [Array](array.md)
- [ArraySlice](arrayslice.md)
- [ClosedRange](closedrange.md)
- [CollectionOfOne](collectionofone.md)
- [ContiguousArray](contiguousarray.md)
- [DefaultIndices](defaultindices.md)
- [EmptyCollection](emptycollection.md)
- [Int.Words](int/words-swift.struct.md)
- [Int16.Words](int16/words-swift.struct.md)
- [Int32.Words](int32/words-swift.struct.md)
- [Int64.Words](int64/words-swift.struct.md)
- [Int8.Words](int8/words-swift.struct.md)
- [KeyValuePairs](keyvaluepairs.md)
- [LazyMapSequence](lazymapsequence.md)
- [LazySequence](lazysequence.md)
- [Range](range.md)
- [RangeSet.Ranges](rangeset/ranges-swift.struct.md)
- [Repeated](repeated.md)
- [ReversedCollection](reversedcollection.md)
- [Slice](slice.md)
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

- [protocol BidirectionalCollection](bidirectionalcollection.md)
  A collection that supports backward as well as forward traversal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/randomaccesscollection)*