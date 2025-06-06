# Sequence Implementations

**Framework**: Create ML Components

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](annotatedfiles/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](annotatedfiles/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](annotatedfiles/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](annotatedfiles/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](annotatedfiles/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(Self.Element) -> Bool](annotatedfiles/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](annotatedfiles/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](annotatedfiles/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](annotatedfiles/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](annotatedfiles/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](annotatedfiles/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](annotatedfiles/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](annotatedfiles/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](annotatedfiles/flatmap(_:)-2dspg.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](annotatedfiles/flatmap(_:)-3dhuv.md)
- [func forEach((Self.Element) throws -> Void) rethrows](annotatedfiles/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted<S>(S) -> S.FormatOutput](annotatedfiles/formatted(_:).md)
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](annotatedfiles/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](annotatedfiles/map(_:)-41kix.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func mapAnnotations<Feature, Input, Output>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Feature, Output>]](annotatedfiles/mapannotations(_:)-2iqz5.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s annotations.
- [func mapAnnotations<Feature, Input, Output>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Feature, Output>]](annotatedfiles/mapannotations(_:)-7rnel.md)
  Returns an array containing the results of mapping the given closure over the sequence’s annotations.
- [func mapFeatures<Input, Output, Annotation>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Output, Annotation>]](annotatedfiles/mapfeatures(_:)-3qook.md)
  Returns an array containing the results of mapping the given closure over the sequence’s features.
- [func mapFeatures<Input, Output, Annotation>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Output, Annotation>]](annotatedfiles/mapfeatures(_:)-5ycje.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s features.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](annotatedfiles/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](annotatedfiles/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func randomSplit<Feature, Annotation>(by: Double, seed: Int?) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](annotatedfiles/randomsplit(by:seed:)-6x4qr.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<T>(by: Double, seed: Int?) -> (ArraySlice<T>, ArraySlice<T>)](annotatedfiles/randomsplit(by:seed:)-77ksg.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func randomSplit<Feature, Annotation, Generator>(by: Double, using: inout Generator) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](annotatedfiles/randomsplit(by:using:)-7afoy.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<T, Generator>(by: Double, using: inout Generator) -> (ArraySlice<T>, ArraySlice<T>)](annotatedfiles/randomsplit(by:using:)-9c84k.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](annotatedfiles/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](annotatedfiles/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reversed() -> [Self.Element]](annotatedfiles/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](annotatedfiles/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](annotatedfiles/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](annotatedfiles/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](annotatedfiles/sorted(using:)-2h836.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](annotatedfiles/sorted(using:)-9lc9a.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](annotatedfiles/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](annotatedfiles/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](annotatedfiles/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles/sequence-implementations)*