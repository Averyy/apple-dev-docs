# Sequence Implementations

**Framework**: Create ML

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](mldatavalue/dictionarytype/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [var publisher: Publishers.Sequence<Self, Never>](mldatavalue/dictionarytype/publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](mldatavalue/dictionarytype/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](mldatavalue/dictionarytype/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](mldatavalue/dictionarytype/compare(_:_:).md)
  If `lhs` is ordered before `rhs` in the ordering described by the given sequence of `SortComparator`s
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](mldatavalue/dictionarytype/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](mldatavalue/dictionarytype/count(where:).md)
  Returns the number of elements in the sequence that satisfy the given predicate.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](mldatavalue/dictionarytype/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func enumerated() -> EnumeratedSequence<Self>](mldatavalue/dictionarytype/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](mldatavalue/dictionarytype/filter(_:)-7s77k.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](mldatavalue/dictionarytype/filter(_:)-c0tf.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatavalue/dictionarytype/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](mldatavalue/dictionarytype/flatmap(_:)-11p5j.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](mldatavalue/dictionarytype/flatmap(_:)-5mw7j.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func forEach((Self.Element) throws -> Void) rethrows](mldatavalue/dictionarytype/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func formatted<S>(S) -> S.FormatOutput](mldatavalue/dictionarytype/formatted(_:).md)
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](mldatavalue/dictionarytype/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](mldatavalue/dictionarytype/map(_:)-1qoo2.md)
  Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [func mapAnnotations<Feature, Input, Output>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Feature, Output>]](mldatavalue/dictionarytype/mapannotations(_:)-13zlx.md)
  Returns an array containing the results of mapping the given closure over the sequence’s annotations.
- [func mapAnnotations<Feature, Input, Output>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Feature, Output>]](mldatavalue/dictionarytype/mapannotations(_:)-2ykxn.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s annotations.
- [func mapFeatures<Input, Output, Annotation>((Input) async throws -> Output) async rethrows -> [AnnotatedFeature<Output, Annotation>]](mldatavalue/dictionarytype/mapfeatures(_:)-3ocap.md)
  Returns an array containing the results of mapping the given async closure over the sequence’s features.
- [func mapFeatures<Input, Output, Annotation>((Input) throws -> Output) rethrows -> [AnnotatedFeature<Output, Annotation>]](mldatavalue/dictionarytype/mapfeatures(_:)-5rlvk.md)
  Returns an array containing the results of mapping the given closure over the sequence’s features.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatavalue/dictionarytype/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatavalue/dictionarytype/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func randomSplit<T>(by: Double, seed: Int?) -> (ArraySlice<T>, ArraySlice<T>)](mldatavalue/dictionarytype/randomsplit(by:seed:)-483qm.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func randomSplit<Feature, Annotation>(by: Double, seed: Int?) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](mldatavalue/dictionarytype/randomsplit(by:seed:)-ljd0.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<Feature, Annotation, Generator>(by: Double, using: inout Generator) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>])](mldatavalue/dictionarytype/randomsplit(by:using:)-8z02p.md)
  Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.
- [func randomSplit<T, Generator>(by: Double, using: inout Generator) -> (ArraySlice<T>, ArraySlice<T>)](mldatavalue/dictionarytype/randomsplit(by:using:)-9mb4k.md)
  Generates two generic arrays by randomly splitting the elements of the sequence.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](mldatavalue/dictionarytype/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](mldatavalue/dictionarytype/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reversed() -> [Self.Element]](mldatavalue/dictionarytype/reversed.md)
  Returns an array containing the elements of this sequence in reverse order.
- [func shuffled() -> [Self.Element]](mldatavalue/dictionarytype/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](mldatavalue/dictionarytype/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](mldatavalue/dictionarytype/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](mldatavalue/dictionarytype/sorted(using:)-2frjp.md)
  Returns the elements of the sequence, sorted using the given comparator to compare elements.
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](mldatavalue/dictionarytype/sorted(using:)-a75q.md)
  Returns the elements of the sequence, sorted using the given array of `SortComparator`s to compare elements.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](mldatavalue/dictionarytype/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](mldatavalue/dictionarytype/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Type Aliases
- [MLDataValue.DictionaryType.Element](mldatavalue/dictionarytype/element.md)
  A type representing the sequence’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/dictionarytype/sequence-implementations)*