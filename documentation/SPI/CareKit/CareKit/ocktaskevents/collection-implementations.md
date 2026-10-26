---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/collection-implementations"
framework: "CareKit/CareKit"
---

# Collection Implementations

**Framework**: CareKit/CareKit  
**Role**: API Collection

## Topics

### Instance Properties
- [var count: Int](./count.md)
- [var first: Self.Element?](./first.md)
- [var indices: DefaultIndices<Self>](./indices.md)
- [var isEmpty: Bool](./isempty.md)
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
- [func indices(where: (Self.Element) throws -> Bool) rethrows -> RangeSet<Self.Index>](./indices%28where%29.md)
- [func map<T, E>((Self.Element) throws(E) -> T) throws(E) -> [T]](./map%28_%29-3jc5i.md)
- [func popFirst() -> Self.Element?](./popfirst%28%29.md)
- [func prefix(Int) -> Self.SubSequence](./prefix%28_%29.md)
- [func prefix(through: Self.Index) -> Self.SubSequence](./prefix%28through%29.md)
- [func prefix(upTo: Self.Index) -> Self.SubSequence](./prefix%28upto%29.md)
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./prefix%28while%29.md)
- [func randomElement() -> Self.Element?](./randomelement%28%29.md)
- [func randomElement<T>(using: inout T) -> Self.Element?](./randomelement%28using%29.md)
- [func removeFirst() -> Self.Element](./removefirst%28%29.md)
- [func removeFirst(Int)](./removefirst%28_%29.md)
- [func removingSubranges(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](./removingsubranges%28_%29.md)
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](./split%28maxsplits,omittingemptysubsequences,whereseparator%29.md)
- [func suffix(Int) -> Self.SubSequence](./suffix%28_%29.md)
- [func suffix(from: Self.Index) -> Self.SubSequence](./suffix%28from%29.md)
- [func trimPrefix(while: (Self.Element) throws -> Bool) throws](./trimprefix%28while%29.md)
- [func trimmingPrefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./trimmingprefix%28while%29.md)
### Subscripts
- [subscript(RangeSet<Self.Index>) -> DiscontiguousSlice<Self>](./subscript%28_%29-5iyz2.md)
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-7ieke.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](./subscript%28_%29-bt8k.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/collection-implementations)*