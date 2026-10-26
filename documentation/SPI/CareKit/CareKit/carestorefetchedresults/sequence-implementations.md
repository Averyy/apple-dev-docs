---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/sequence-implementations"
framework: "CareKit/CareKit"
---

# Sequence Implementations

**Framework**: CareKit/CareKit  
**Role**: API Collection

## Topics

### Instance Properties
- [var async: AsyncSyncSequence<Self>](./async.md)
- [var lazy: LazySequence<Self>](./lazy.md)
- [var publisher: Publishers.Sequence<Self, Never>](./publisher.md)
### Instance Methods
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](./allsatisfy%28_%29.md)
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](./compactmap%28_%29.md)
- [func compare<Comparator>(Comparator.Compared, Comparator.Compared) -> ComparisonResult](./compare%28_,_%29.md)
- [func contains(Self.Element) -> Bool](./contains%28_%29-92exe.md)
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](./contains%28where%29.md)
- [func count<E>(where: (Self.Element) throws(E) -> Bool) throws(E) -> Int](./count%28where%29.md)
- [func donatedWithin<DonationInfo>(Tips.DonationTimeRange) -> [Self.Element]](./donatedwithin%28_%29.md)
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](./elementsequal%28_%29.md)
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](./elementsequal%28_,by%29.md)
- [func enumerated() -> EnumeratedSequence<Self>](./enumerated%28%29.md)
- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](./filter%28_%29-1kohz.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](./filter%28_%29-9fk50.md)
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](./first%28where%29.md)
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](./flatmap%28_%29-8r3rc.md)
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](./flatmap%28_%29-9nwc7.md)
- [func forEach((Self.Element) throws -> Void) rethrows](./foreach%28_%29.md)
- [func formatted<S>(S) -> S.FormatOutput](./formatted%28_%29.md)
- [func largestSubset<DonationInfo, Value>(groupedBy: KeyPath<DonationInfo, Value>) -> [Self.Element]](./largestsubset%28groupedby%29.md)
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](./lexicographicallyprecedes%28_,by%29.md)
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](./map%28_%29-9au17.md)
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./max%28by%29.md)
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](./min%28by%29.md)
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](./reduce%28_,_%29.md)
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](./reduce%28into,_%29.md)
- [func shuffled() -> [Self.Element]](./shuffled%28%29.md)
- [func shuffled<T>(using: inout T) -> [Self.Element]](./shuffled%28using%29.md)
- [func smallestSubset<DonationInfo, Value>(groupedBy: KeyPath<DonationInfo, Value>) -> [Self.Element]](./smallestsubset%28groupedby%29.md)
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](./sorted%28by%29.md)
- [func sorted<Comparator>(using: Comparator) -> [Self.Element]](./sorted%28using%29-5maxo.md)
- [func sorted<S, Comparator>(using: S) -> [Self.Element]](./sorted%28using%29-vvk8.md)
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](./split%28separator,maxsplits,omittingemptysubsequences%29-5exkz.md)
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](./starts%28with%29.md)
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](./starts%28with,by%29.md)
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousstorageifavailable%28_%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults/sequence-implementations)*