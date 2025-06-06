# Sequence

**Framework**: Swift  
**Kind**: protocol

A type that provides sequential, iterated access to its elements.

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
protocol Sequence<Element>
```

#### Overview

A sequence is a list of values that you can step through one at a time. The most common way to iterate over the elements of a sequence is to use a `for`-`in` loop:

```swift
let oneTwoThree = 1...3
for number in oneTwoThree {
    print(number)
}
// Prints "1"
// Prints "2"
// Prints "3"
```

While seemingly simple, this capability gives you access to a large number of operations that you can perform on any sequence. As an example, to check whether a sequence includes a particular value, you can test each value sequentially until you’ve found a match or reached the end of the sequence. This example checks to see whether a particular insect is in an array.

```swift
let bugs = ["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]
var hasMosquito = false
for bug in bugs {
    if bug == "Mosquito" {
        hasMosquito = true
        break
    }
}
print("'bugs' has a mosquito: \(hasMosquito)")
// Prints "'bugs' has a mosquito: false"
```

The `Sequence` protocol provides default implementations for many common operations that depend on sequential access to a sequence’s values. For clearer, more concise code, the example above could use the array’s `contains(_:)` method, which every sequence inherits from `Sequence`, instead of iterating manually:

```swift
if bugs.contains("Mosquito") {
    print("Break out the bug spray.")
} else {
    print("Whew, no mosquitos!")
}
// Prints "Whew, no mosquitos!"
```

### Repeated Access

The `Sequence` protocol makes no requirement on conforming types regarding whether they will be destructively consumed by iteration. As a consequence, don’t assume that multiple `for`-`in` loops on a sequence will either resume iteration or restart from the beginning:

```swift
for element in sequence {
    if ... some condition { break }
}

for element in sequence {
    // No defined behavior
}
```

In this case, you cannot assume either that a sequence will be consumable and will resume iteration, or that a sequence is a collection and will restart iteration from the first element. A conforming sequence that is not a collection is allowed to produce an arbitrary sequence of elements in the second `for`-`in` loop.

To establish that a type you’ve created supports nondestructive iteration, add conformance to the `Collection` protocol.

### Conforming to the Sequence Protocol

Making your own custom types conform to `Sequence` enables many useful operations, like `for`-`in` looping and the `contains` method, without much effort. To add `Sequence` conformance to your own custom type, add a `makeIterator()` method that returns an iterator.

Alternatively, if your type can act as its own iterator, implementing the requirements of the `IteratorProtocol` protocol and declaring conformance to both `Sequence` and `IteratorProtocol` are sufficient.

Here’s a definition of a `Countdown` sequence that serves as its own iterator. The `makeIterator()` method is provided as a default implementation.

```swift
struct Countdown: Sequence, IteratorProtocol {
    var count: Int

    mutating func next() -> Int? {
        if count == 0 {
            return nil
        } else {
            defer { count -= 1 }
            return count
        }
    }
}

let threeToGo = Countdown(count: 3)
for i in threeToGo {
    print(i)
}
// Prints "3"
// Prints "2"
// Prints "1"
```

### Expected Performance

A sequence should provide its iterator in O(1). The `Sequence` protocol makes no other requirements about element access, so routines that traverse a sequence should be considered O() unless documented otherwise.

## Topics

### Creating an Iterator
- [func makeIterator() -> Self.Iterator](sequence/makeiterator.md)
  Returns an iterator over the elements of this sequence.
- [associatedtype Iterator : IteratorProtocol](sequence/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.
- [associatedtype Element](sequence/element.md)
  A type representing the sequence’s elements.
### Finding Elements
- [func contains(Self.Element) -> Bool](sequence/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](sequence/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](sequence/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](sequence/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func min() -> Self.Element?](sequence/min.md)
  Returns the minimum element in the sequence.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](sequence/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max() -> Self.Element?](sequence/max.md)
  Returns the maximum element in the sequence.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](sequence/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
### Selecting Elements
- [func prefix(Int) -> PrefixSequence<Self>](sequence/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](sequence/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func suffix(Int) -> [Self.Element]](sequence/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
### Excluding Elements
- [func dropFirst(Int) -> DropFirstSequence<Self>](sequence/dropfirst(_:).md)
  Returns a sequence containing all but the given number of initial elements.
- [func dropLast(Int) -> [Self.Element]](sequence/droplast(_:).md)
  Returns a sequence containing all but the given number of final elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](sequence/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](sequence/filter(_:)-5y9d2.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
### Transforming a Sequence
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](sequence/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](sequence/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](sequence/flatmap(_:)-jo2y.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](sequence/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](sequence/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](sequence/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](sequence/flatmap(_:)-383uq.md)
### Iterating Over a Sequence’s Elements
- [func forEach((Self.Element) throws -> Void) rethrows](sequence/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](sequence/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var underestimatedCount: Int](sequence/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Sorting Elements
- [func sorted() -> [Self.Element]](sequence/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](sequence/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reversed() -> [Self.Element]](sequence/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
### Reordering a Sequence’s Elements
- [func shuffled() -> [Self.Element]](sequence/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](sequence/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Formatting a Sequence
- [func formatted() -> String](sequence/formatted.md)
- [func formatted<S>(S) -> S.FormatOutput](sequence/formatted(_:).md)
- [struct ListFormatStyle<Style, Base> where Style : FormatStyle, Base : Sequence, Style.FormatInput == Base.Element, Style.FormatOutput == String](../Foundation/ListFormatStyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.
### Splitting and Joining Elements
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](sequence/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](sequence/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func joined() -> FlattenSequence<Self>](sequence/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined(separator: String) -> String](sequence/joined(separator:)-5zjyj.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](sequence/joined(separator:)-7w47r.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
### Comparing Sequences
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](sequence/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](sequence/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](sequence/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](sequence/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](sequence/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](sequence/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Accessing Underlying Storage
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](sequence/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Publishing a Sequence
- [var publisher: Publishers.Sequence<Self, Never>](sequence/publisher.md)
### Applying AppKit Graphic Operations
- [func fill(using: NSCompositingOperation)](sequence/fill(using:)-l1te.md)
  Fills this list of rects in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [func fill(using: NSCompositingOperation)](sequence/fill(using:)-45en6.md)
  Fills this list of rects in the current NSGraphicsContext with that rect’s associated color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [func clip()](sequence/clip.md)
  Modifies the current graphics context clipping path by intersecting it with the graphical union of this list of rects This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.
### Instance Methods
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](sequence/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](sequence/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func donatedWithin<DonationInfo>(Tips.DonationTimeRange) -> [Self.Element]](sequence/donatedwithin(_:).md)
- [func fill(using: NSCompositingOperation)](sequence/fill(using:)-6sdhf.md)
  Fills this list of rects in the current NSGraphicsContext with that rect’s associated gray component value in the DeviceGray color space. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFillListWithGrays()`.
- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](sequence/filter(_:)-8li9y.md)
- [func filter<T>(matchingCategory: CMTypedTag<T>.Category) -> [CMTypedTag<T>]](sequence/filter(matchingcategory:).md)
  Filters a sequence of tags based on matching the specified category.  Returns the tags that match the specified category.
- [func first<T>(matchingCategory: CMTypedTag<T>.Category) -> CMTypedTag<T>?](sequence/first(matchingcategory:).md)
  Finds and returns the first tag matching the specified category.
- [func firstValue<T>(matchingCategory: CMTypedTag<T>.Category) -> T?](sequence/firstvalue(matchingcategory:).md)
  Finds the first tag matching the specified category and returns the value of the matching tag.
- [func largestSubset<DonationInfo, Value>(groupedBy: KeyPath<DonationInfo, Value>) -> [Self.Element]](sequence/largestsubset(groupedby:).md)
- [func mapAnnotations<Feature, Input, Output>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Feature, Output>]](sequence/mapannotations(_:)-48olp.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s annotations.
- [func mapAnnotations<Feature, Input, Output>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Feature, Output>]](sequence/mapannotations(_:)-9q4pb.md)
  Returns an array containing the results of mapping the given closure over the sequence’s annotations.
- [func mapFeatures<Input, Output, Annotation>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Output, Annotation>]](sequence/mapfeatures(_:)-83n0d.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s features.
- [func mapFeatures<Input, Output, Annotation>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Output, Annotation>]](sequence/mapfeatures(_:)-8zq1h.md)
  Returns an array containing the results of mapping the given closure over the sequence’s features.
- [func randomSplit<Feature, Annotation>(by: Double, seed: Int?) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](sequence/randomsplit(by:seed:)-3a1xo.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<T>(by: Double, seed: Int?) -> (ArraySlice<T>, ArraySlice<T>)](sequence/randomsplit(by:seed:)-9637d.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func randomSplit<T, Generator>(by: Double, using: inout Generator) -> (ArraySlice<T>, ArraySlice<T>)](sequence/randomsplit(by:using:)-500fy.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func randomSplit<Feature, Annotation, Generator>(by: Double, using: inout Generator) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](sequence/randomsplit(by:using:)-9i5e5.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func smallestSubset<DonationInfo, Value>(groupedBy: KeyPath<DonationInfo, Value>) -> [Self.Element]](sequence/smallestsubset(groupedby:).md)
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](sequence/sorted(using:)-69w5u.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](sequence/sorted(using:)-95lls.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
### Type Methods
- [static func reparentEquipment(some Sequence<any Equipment>, childrenOf: some Equipment, order: MoveEquipmentAction.Order?, context: UInt64) -> Self](sequence/reparentequipment(_:childrenof:order:context:).md)
- [static func reparentEquipment(matching: some Sequence<EquipmentIdentifier>, childrenOf: EquipmentIdentifier, order: MoveEquipmentAction.Order?, context: UInt64) -> Self](sequence/reparentequipment(matching:childrenof:order:context:).md)

## Relationships

### Inherited By
- [BidirectionalCollection](bidirectionalcollection.md)
- [Collection](collection.md)
- [LazyCollectionProtocol](lazycollectionprotocol.md)
- [LazySequenceProtocol](lazysequenceprotocol.md)
- [MutableCollection](mutablecollection.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [RangeReplaceableCollection](rangereplaceablecollection.md)
- [StringProtocol](stringprotocol.md)
### Conforming Types
- [AnyBidirectionalCollection](anybidirectionalcollection.md)
- [AnyCollection](anycollection.md)
- [AnyIterator](anyiterator.md)
- [AnyRandomAccessCollection](anyrandomaccesscollection.md)
- [AnyRegexOutput](anyregexoutput.md)
- [AnySequence](anysequence.md)
- [Array](array.md)
- [ArraySlice](arrayslice.md)
- [ClosedRange](closedrange.md)
- [CollectionDifference](collectiondifference.md)
- [CollectionOfOne](collectionofone.md)
- [ContiguousArray](contiguousarray.md)
- [DefaultIndices](defaultindices.md)
- [Dictionary](dictionary.md)
- [Dictionary.Keys](dictionary/keys-swift.struct.md)
- [Dictionary.Values](dictionary/values-swift.struct.md)
- [DiscontiguousSlice](discontiguousslice.md)
- [DropFirstSequence](dropfirstsequence.md)
- [DropWhileSequence](dropwhilesequence.md)
- [EmptyCollection](emptycollection.md)
- [EmptyCollection.Iterator](emptycollection/iterator.md)
- [EnumeratedSequence](enumeratedsequence.md)
- [EnumeratedSequence.Iterator](enumeratedsequence/iterator.md)
- [FlattenSequence](flattensequence.md)
- [FlattenSequence.Iterator](flattensequence/iterator.md)
- [IndexingIterator](indexingiterator.md)
- [Int.Words](int/words-swift.struct.md)
- [Int16.Words](int16/words-swift.struct.md)
- [Int32.Words](int32/words-swift.struct.md)
- [Int64.Words](int64/words-swift.struct.md)
- [Int8.Words](int8/words-swift.struct.md)
- [IteratorSequence](iteratorsequence.md)
- [JoinedSequence](joinedsequence.md)
- [KeyValuePairs](keyvaluepairs.md)
- [LazyDropWhileSequence](lazydropwhilesequence.md)
- [LazyFilterSequence](lazyfiltersequence.md)
- [LazyFilterSequence.Iterator](lazyfiltersequence/iterator.md)
- [LazyMapSequence](lazymapsequence.md)
- [LazyMapSequence.Iterator](lazymapsequence/iterator.md)
- [LazyPrefixWhileSequence](lazyprefixwhilesequence.md)
- [LazyPrefixWhileSequence.Iterator](lazyprefixwhilesequence/iterator.md)
- [LazySequence](lazysequence.md)
- [PartialRangeFrom](partialrangefrom.md)
- [PrefixSequence](prefixsequence.md)
- [Range](range.md)
- [RangeSet.Ranges](rangeset/ranges-swift.struct.md)
- [Repeated](repeated.md)
- [ReversedCollection](reversedcollection.md)
- [ReversedCollection.Iterator](reversedcollection/iterator.md)
- [Set](set.md)
- [Slice](slice.md)
- [StrideThrough](stridethrough.md)
- [StrideTo](strideto.md)
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
- [UnfoldSequence](unfoldsequence.md)
- [Unicode.Scalar.UTF16View](unicode/scalar/utf16view.md)
- [Unicode.Scalar.UTF8View](unicode/scalar/utf8view.md)
- [UnsafeBufferPointer](unsafebufferpointer.md)
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md)
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md)
- [UnsafeRawBufferPointer.Iterator](unsaferawbufferpointer/iterator.md)
- [Zip2Sequence](zip2sequence.md)

## See Also

- [protocol Collection](collection.md)
  A sequence whose elements can be traversed multiple times, nondestructively, and accessed by an indexed subscript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence)*