---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain2sequence/asyncsequence-implementations"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncSequence Implementations

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Role**: API Collection

## Topics

### Instance Methods
- [func allSatisfy((Self.Element) async throws -> Bool) async rethrows -> Bool](./allsatisfy%28_%29.md)
- [func compactMap<ElementOfResult>((Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-21ibv.md)
- [func compactMap<ElementOfResult>((Self.Element) async throws -> ElementOfResult?) -> AsyncThrowingCompactMapSequence<Self, ElementOfResult>](./compactmap%28_%29-47dj.md)
- [func contains(Self.Element) async rethrows -> Bool](./contains%28_%29.md)
- [func contains(where: (Self.Element) async throws -> Bool) async rethrows -> Bool](./contains%28where%29.md)
- [func drop(while: (Self.Element) async -> Bool) -> AsyncDropWhileSequence<Self>](./drop%28while%29.md)
- [func dropFirst(Int) -> AsyncDropFirstSequence<Self>](./dropfirst%28_%29.md)
- [func filter((Self.Element) async -> Bool) -> AsyncFilterSequence<Self>](./filter%28_%29.md)
- [func first(where: (Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./first%28where%29.md)
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-2jh27.md)
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-336xw.md)
- [func flatMap<SegmentOfResult>((Self.Element) async throws -> SegmentOfResult) -> AsyncThrowingFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-511jm.md)
- [func flatMap<SegmentOfResult>((Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult>](./flatmap%28_%29-5jv4a.md)
- [func makeAsyncIterator() -> AsyncChain2Sequence<Base1, Base2>.Iterator](./makeasynciterator%28%29.md)
- [func map<Transformed>((Self.Element) async -> Transformed) -> AsyncMapSequence<Self, Transformed>](./map%28_%29-7nk1f.md)
- [func map<Transformed>((Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>](./map%28_%29-900ww.md)
- [func max() async rethrows -> Self.Element?](./max%28%29.md)
- [func max(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./max%28by%29.md)
- [func min() async rethrows -> Self.Element?](./min%28%29.md)
- [func min(by: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?](./min%28by%29.md)
- [func prefix(Int) -> AsyncPrefixSequence<Self>](./prefix%28_%29.md)
- [func prefix(while: (Self.Element) async -> Bool) rethrows -> AsyncPrefixWhileSequence<Self>](./prefix%28while%29.md)
- [func reduce<Result>(Result, (Result, Self.Element) async throws -> Result) async rethrows -> Result](./reduce%28_,_%29.md)
- [func reduce<Result>(into: Result, (inout Result, Self.Element) async throws -> Void) async rethrows -> Result](./reduce%28into,_%29.md)
### Type Aliases
- [AsyncChain2Sequence.Element](./element.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncchain2sequence/asyncsequence-implementations)*