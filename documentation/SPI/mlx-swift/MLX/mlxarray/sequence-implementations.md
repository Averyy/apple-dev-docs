---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/sequence-implementations"
framework: "mlx-swift/MLX"
---

# Sequence Implementations

**Framework**: mlx-swift/MLX  
**Role**: API Collection

## Topics

### Instance Properties
- [var lazy: LazySequence<Self>](./lazy.md)
- [var publisher: Publishers.Sequence<Self, Never>](./publisher.md)
- [var underestimatedCount: Int](./underestimatedcount.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](./allsatisfy%28_%29.md)
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](./compactmap%28_%29.md)
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](./compare%28_,_%29.md)
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](./contains%28where%29.md)
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](./count%28where%29.md)
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> DropWhileSequence<Self>](./drop%28while%29.md)
- [func dropFirst(Int) -> DropFirstSequence<Self>](./dropfirst%28_%29.md)
- [func dropLast(Int) -> [Self.Element]](./droplast%28_%29.md)
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](./elementsequal%28_,by%29.md)
- [func enumerated() -> EnumeratedSequence<Self>](./enumerated%28%29.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](./filter%28_%29.md)
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./first%28where%29.md)
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](./flatmap%28_%29-1ghyp.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](./flatmap%28_%29-nya7.md)
- [func forEach((Self.Element) throws -> Void) rethrows](./foreach%28_%29.md)
- [func formatted<S>(S) -> S.FormatOutput](./formatted%28_%29.md)
- [func joined() -> FlattenSequence<Self>](./joined%28%29.md)
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](./joined%28separator%29.md)
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](./lexicographicallyprecedes%28_,by%29.md)
- [func makeIterator() -> some IteratorProtocol<MLXArray>
](./makeiterator%28%29.md)
  Return an iterator along axis 0:
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](./map%28_%29.md)
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./max%28by%29.md)
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./min%28by%29.md)
- [func prefix(Int) -> PrefixSequence<Self>](./prefix%28_%29.md)
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](./prefix%28while%29.md)
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](./reduce%28_,_%29.md)
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](./reduce%28into,_%29.md)
- [func reversed() -> [Self.Element]](./reversed%28%29.md)
- [func shuffled() -> [Self.Element]](./shuffled%28%29.md)
- [func shuffled<T>(using: inout T) -> [Self.Element]](./shuffled%28using%29.md)
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](./sorted%28by%29.md)
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](./sorted%28using%29-24lgs.md)
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](./sorted%28using%29-91uyg.md)
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](./split%28maxsplits,omittingemptysubsequences,whereseparator%29.md)
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](./starts%28with,by%29.md)
- [func suffix(Int) -> [Self.Element]](./suffix%28_%29.md)
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousstorageifavailable%28_%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/sequence-implementations)*