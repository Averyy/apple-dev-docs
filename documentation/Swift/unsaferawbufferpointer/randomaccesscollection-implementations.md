# RandomAccessCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func distance(from: Self.Index, to: Self.Index) -> Self.Index.Stride](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [func index(Self.Index, offsetBy: Self.Index.Stride) -> Self.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func index(after: Self.Index) -> Self.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func index(before: Self.Index) -> Self.Index](./index%28before%29.md)
  Returns the position immediately after the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer/randomaccesscollection-implementations)*