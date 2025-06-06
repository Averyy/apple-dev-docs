# MLDataTable.Rows

**Framework**: Create ML  
**Kind**: struct

A collection of rows in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Rows
```

## Topics

### Inspecting a row collection
- [var isEmpty: Bool](mldatatable/rows-swift.struct/isempty.md)
  A Boolean value indicating whether the collection is empty.
- [var count: Int](mldatatable/rows-swift.struct/count.md)
  The number of elements in the collection.
### Accessing rows
- [subscript(Int) -> MLDataTable.Rows.Element](mldatatable/rows-swift.struct/subscript(_:).md)
  Subscript by index. This returns a row in the data table.
- [var first: Self.Element?](mldatatable/rows-swift.struct/first.md)
  The first element of the collection.
- [var last: Self.Element?](mldatatable/rows-swift.struct/last.md)
  The last element of the collection.
- [func randomElement() -> Self.Element?](mldatatable/rows-swift.struct/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](mldatatable/rows-swift.struct/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
### Finding rows
- [func contains(Self.Element) -> Bool](mldatatable/rows-swift.struct/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](mldatatable/rows-swift.struct/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatatable/rows-swift.struct/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](mldatatable/rows-swift.struct/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatatable/rows-swift.struct/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
### Selecting rows
- [func prefix(Int) -> Self.SubSequence](mldatatable/rows-swift.struct/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](mldatatable/rows-swift.struct/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](mldatatable/rows-swift.struct/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatatable/rows-swift.struct/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](mldatatable/rows-swift.struct/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](mldatatable/rows-swift.struct/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Excluding rows
- [func dropFirst(Int) -> Self.SubSequence](mldatatable/rows-swift.struct/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](mldatatable/rows-swift.struct/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](mldatatable/rows-swift.struct/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
### Transforming a row collection
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](mldatatable/rows-swift.struct/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](mldatatable/rows-swift.struct/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](mldatatable/rows-swift.struct/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
### Iterating over a row collection’s rows
- [func forEach((Self.Element) throws -> Void) rethrows](mldatatable/rows-swift.struct/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](mldatatable/rows-swift.struct/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func makeIterator() -> IndexingIterator<Self>](mldatatable/rows-swift.struct/makeiterator.md)
  Returns an iterator over the elements of the collection.
### Reordering a row collection’s rows
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](mldatatable/rows-swift.struct/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reversed() -> ReversedCollection<Self>](mldatatable/rows-swift.struct/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func shuffled() -> [Self.Element]](mldatatable/rows-swift.struct/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](mldatatable/rows-swift.struct/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Splitting and joining rows
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](mldatatable/rows-swift.struct/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](mldatatable/rows-swift.struct/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](mldatatable/rows-swift.struct/joined(separator:).md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
### Comparing row collections
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](mldatatable/rows-swift.struct/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](mldatatable/rows-swift.struct/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Manipulating indices
- [var startIndex: Int](mldatatable/rows-swift.struct/startindex.md)
  The position of the first row in a nonempty DataTable. If the DataTable is empty, `startIndex` is equal to `endIndex`.
- [var endIndex: Int](mldatatable/rows-swift.struct/endindex.md)
  The DataTable’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func formIndex(after: inout Self.Index)](mldatatable/rows-swift.struct/formindex(after:).md)
  Replaces the given index with its successor.
- [func formIndex(before: inout Self.Index)](mldatatable/rows-swift.struct/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(inout Self.Index, offsetBy: Int)](mldatatable/rows-swift.struct/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](mldatatable/rows-swift.struct/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](mldatatable/rows-swift.struct/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
### Describing a row collection
- [var description: String](mldatatable/rows-swift.struct/description.md)
  A textual representation of this instance.
- [var debugDescription: String](mldatatable/rows-swift.struct/debugdescription.md)
  A textual representation of this instance, suitable for debugging.
- [var playgroundDescription: Any](mldatatable/rows-swift.struct/playgrounddescription.md)
  A custom playground description for this instance.
### Supporting types
- [MLDataTable.Row](mldatatable/row.md)
  A row of untyped values in a data table.
- [MLDataTable.Rows.Element](mldatatable/rows-swift.struct/element.md)
  The Element of a DataTable is a Row. This is represented as a Dictionary-like type containing all Column names and their corresponding values.
### Default Implementations
- [BidirectionalCollection Implementations](mldatatable/rows-swift.struct/bidirectionalcollection-implementations.md)
- [Collection Implementations](mldatatable/rows-swift.struct/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](mldatatable/rows-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldatatable/rows-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldatatable/rows-swift.struct/customstringconvertible-implementations.md)
- [RandomAccessCollection Implementations](mldatatable/rows-swift.struct/randomaccesscollection-implementations.md)
- [Sequence Implementations](mldatatable/rows-swift.struct/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var rows: MLDataTable.Rows](mldatatable/rows-swift.property.md)
  The rows of data in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct)*