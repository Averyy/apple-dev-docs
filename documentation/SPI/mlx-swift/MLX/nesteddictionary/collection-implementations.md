---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/collection-implementations"
framework: "mlx-swift/MLX"
---

# Collection Implementations

**Framework**: mlx-swift/MLX  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: NestedDictionary<Key, Element>.Index](./endindex.md)
- [var first: Self.Element?](./first.md)
- [var indices: DefaultIndices<Self>](./indices.md)
- [var startIndex: NestedDictionary<Key, Element>.Index](./startindex.md)
- [var underestimatedCount: Int](./underestimatedcount.md)
### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Int](./distance%28from,to%29.md)
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./drop%28while%29.md)
- [func dropFirst(Int) -> Self.SubSequence](./dropfirst%28_%29.md)
- [func dropLast(Int) -> Self.SubSequence](./droplast%28_%29.md)
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](./firstindex%28where%29.md)
- [func formIndex(inout Self.Index, offsetBy: Int)](./formindex%28_,offsetby%29.md)
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](./formindex%28_,offsetby,limitedby%29.md)
- [func formIndex(after: inout Self.Index)](./formindex%28after%29.md)
- [func index(Self.Index, offsetBy: Int) -> Self.Index](./index%28_,offsetby%29.md)
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](./index%28_,offsetby,limitedby%29.md)
- [func index(after: NestedDictionary<Key, Element>.Index) -> NestedDictionary<Key, Element>.Index](./index%28after%29.md)
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](./indices%28where%29.md)
- [func makeIterator() -> IndexingIterator<Self>](./makeiterator%28%29.md)
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](./map%28_%29-4wclo.md)
- [func prefix(Int) -> Self.SubSequence](./prefix%28_%29.md)
- [func prefix(through: Self.Index) -> Self.SubSequence](./prefix%28through%29.md)
- [func prefix(upTo: Self.Index) -> Self.SubSequence](./prefix%28upto%29.md)
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./prefix%28while%29.md)
- [func randomElement() -> Self.Element?](./randomelement%28%29.md)
- [func randomElement<T>(using: inout T) -> Self.Element?](./randomelement%28using%29.md)
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](./removingsubranges%28_%29.md)
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](./split%28maxsplits,omittingemptysubsequences,whereseparator%29.md)
- [func suffix(Int) -> Self.SubSequence](./suffix%28_%29.md)
- [func suffix(from: Self.Index) -> Self.SubSequence](./suffix%28from%29.md)
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./trimmingprefix%28while%29.md)
### Subscripts
- [subscript(Range<Self.Index>) -> Slice<Self>](./subscript%28_%29-27we2.md)
- [subscript(NestedDictionary<Key, Element>.Index) -> NestedDictionary<Key, Element>.CollectionElement](./subscript%28_%29-4t8fg.md)
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-5jt9z.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](./subscript%28_%29-6pveg.md)
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](./subscript%28_%29-917n5.md)
### Type Aliases
- [NestedDictionary.Index](./index.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/collection-implementations)*