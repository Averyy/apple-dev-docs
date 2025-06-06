# Sequence Implementations

**Framework**: Create ML

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](mldatatable/row/values-swift.struct/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](mldatatable/row/values-swift.struct/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/row/values-swift.struct/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](mldatatable/row/values-swift.struct/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](mldatatable/row/values-swift.struct/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(Self.Element) -> Bool](mldatatable/row/values-swift.struct/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/row/values-swift.struct/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](mldatatable/row/values-swift.struct/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](mldatatable/row/values-swift.struct/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](mldatatable/row/values-swift.struct/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](mldatatable/row/values-swift.struct/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](mldatatable/row/values-swift.struct/filter(_:)-3ii0s.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](mldatatable/row/values-swift.struct/filter(_:)-4ae4h.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/row/values-swift.struct/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](mldatatable/row/values-swift.struct/flatmap(_:)-25drg.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](mldatatable/row/values-swift.struct/flatmap(_:)-76jjn.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](mldatatable/row/values-swift.struct/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted<S>(S) -> S.FormatOutput](mldatatable/row/values-swift.struct/formatted(_:).md)
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/row/values-swift.struct/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](mldatatable/row/values-swift.struct/map(_:)-9ujyp.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func mapAnnotations<Feature, Input, Output>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Feature, Output>]](mldatatable/row/values-swift.struct/mapannotations(_:)-9umkf.md)
  Returns an array containing the results of mapping the given closure over the sequence’s annotations.
- [func mapAnnotations<Feature, Input, Output>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Feature, Output>]](mldatatable/row/values-swift.struct/mapannotations(_:)-lv6t.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s annotations.
- [func mapFeatures<Input, Output, Annotation>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Output, Annotation>]](mldatatable/row/values-swift.struct/mapfeatures(_:)-2y24e.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s features.
- [func mapFeatures<Input, Output, Annotation>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Output, Annotation>]](mldatatable/row/values-swift.struct/mapfeatures(_:)-6zhmj.md)
  Returns an array containing the results of mapping the given closure over the sequence’s features.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/row/values-swift.struct/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/row/values-swift.struct/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func randomSplit<T>(by: Double, seed: Int?) -> (ArraySlice<T>, ArraySlice<T>)](mldatatable/row/values-swift.struct/randomsplit(by:seed:)-59n47.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func randomSplit<Feature, Annotation>(by: Double, seed: Int?) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](mldatatable/row/values-swift.struct/randomsplit(by:seed:)-5x1av.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<T, Generator>(by: Double, using: inout Generator) -> (ArraySlice<T>, ArraySlice<T>)](mldatatable/row/values-swift.struct/randomsplit(by:using:)-1rf7x.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func randomSplit<Feature, Annotation, Generator>(by: Double, using: inout Generator) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](mldatatable/row/values-swift.struct/randomsplit(by:using:)-89k4w.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](mldatatable/row/values-swift.struct/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](mldatatable/row/values-swift.struct/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func shuffled() -> [Self.Element]](mldatatable/row/values-swift.struct/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](mldatatable/row/values-swift.struct/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](mldatatable/row/values-swift.struct/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](mldatatable/row/values-swift.struct/sorted(using:)-37sf7.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](mldatatable/row/values-swift.struct/sorted(using:)-ph76.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](mldatatable/row/values-swift.struct/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](mldatatable/row/values-swift.struct/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](mldatatable/row/values-swift.struct/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/values-swift.struct/sequence-implementations)*