# Sequence Implementations

**Framework**: Create ML Components

## Topics

### Structures
- [TimeSeriesForecasterAnnotatedWindows.Iterator](timeseriesforecasterannotatedwindows/iterator.md)
  A time-series forecaster batch sequence iterator.
### Instance Properties
- [var lazy: LazySequence<Self>](timeseriesforecasterannotatedwindows/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](timeseriesforecasterannotatedwindows/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](timeseriesforecasterannotatedwindows/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](timeseriesforecasterannotatedwindows/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](timeseriesforecasterannotatedwindows/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(Self.Element) -> Bool](timeseriesforecasterannotatedwindows/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](timeseriesforecasterannotatedwindows/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](timeseriesforecasterannotatedwindows/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](timeseriesforecasterannotatedwindows/drop(while:).md)
  Returns a sequence by skipping the initial, consecutive elements that satisfy the given predicate.
- [func dropFirst(Int) -> DropFirstSequence<Self>](timeseriesforecasterannotatedwindows/dropfirst(_:).md)
  Returns a sequence containing all but the given number of initial elements.
- [func dropLast(Int) -> [Self.Element]](timeseriesforecasterannotatedwindows/droplast(_:).md)
  Returns a sequence containing all but the given number of final elements.
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](timeseriesforecasterannotatedwindows/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](timeseriesforecasterannotatedwindows/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](timeseriesforecasterannotatedwindows/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](timeseriesforecasterannotatedwindows/filter(_:).md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](timeseriesforecasterannotatedwindows/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](timeseriesforecasterannotatedwindows/flatmap(_:)-7jtd0.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](timeseriesforecasterannotatedwindows/flatmap(_:)-9fprr.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](timeseriesforecasterannotatedwindows/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted<S>(S) -> S.FormatOutput](timeseriesforecasterannotatedwindows/formatted(_:).md)
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](timeseriesforecasterannotatedwindows/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](timeseriesforecasterannotatedwindows/map(_:).md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func mapAnnotations<Feature, Input, Output>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Feature, Output>]](timeseriesforecasterannotatedwindows/mapannotations(_:)-3hvv4.md)
  Returns an array containing the results of mapping the given closure over the sequence’s annotations.
- [func mapAnnotations<Feature, Input, Output>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Feature, Output>]](timeseriesforecasterannotatedwindows/mapannotations(_:)-4kqar.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s annotations.
- [func mapFeatures<Input, Output, Annotation>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Output, Annotation>]](timeseriesforecasterannotatedwindows/mapfeatures(_:)-3kejb.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s features.
- [func mapFeatures<Input, Output, Annotation>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Output, Annotation>]](timeseriesforecasterannotatedwindows/mapfeatures(_:)-84p11.md)
  Returns an array containing the results of mapping the given closure over the sequence’s features.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](timeseriesforecasterannotatedwindows/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](timeseriesforecasterannotatedwindows/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func prefix(Int) -> PrefixSequence<Self>](timeseriesforecasterannotatedwindows/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](timeseriesforecasterannotatedwindows/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func randomSplit<Feature, Annotation>(by: Double, seed: Int?) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](timeseriesforecasterannotatedwindows/randomsplit(by:seed:)-2txef.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<T>(by: Double, seed: Int?) -> (ArraySlice<T>, ArraySlice<T>)](timeseriesforecasterannotatedwindows/randomsplit(by:seed:)-6drmr.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func randomSplit<Feature, Annotation, Generator>(by: Double, using: inout Generator) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](timeseriesforecasterannotatedwindows/randomsplit(by:using:)-47jq5.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<T, Generator>(by: Double, using: inout Generator) -> (ArraySlice<T>, ArraySlice<T>)](timeseriesforecasterannotatedwindows/randomsplit(by:using:)-4fsb0.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](timeseriesforecasterannotatedwindows/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](timeseriesforecasterannotatedwindows/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reversed() -> [Self.Element]](timeseriesforecasterannotatedwindows/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](timeseriesforecasterannotatedwindows/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](timeseriesforecasterannotatedwindows/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](timeseriesforecasterannotatedwindows/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](timeseriesforecasterannotatedwindows/sorted(using:)-2j30.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](timeseriesforecasterannotatedwindows/sorted(using:)-8o8av.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](timeseriesforecasterannotatedwindows/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](timeseriesforecasterannotatedwindows/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](timeseriesforecasterannotatedwindows/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](timeseriesforecasterannotatedwindows/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func suffix(Int) -> [Self.Element]](timeseriesforecasterannotatedwindows/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](timeseriesforecasterannotatedwindows/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterannotatedwindows/sequence-implementations)*