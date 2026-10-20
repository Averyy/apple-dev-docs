# RandomAccessCollection Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var endIndex: KeyValuePairs<Key, Value>.Index](./endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Range<Self.Index>](./indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: KeyValuePairs<Key, Value>.Index](./startindex.md)
  The position of the first element in a nonempty collection.
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
### Subscripts
- [subscript(KeyValuePairs<Key, Value>.Index) -> KeyValuePairs<Key, Value>.Element](./subscript%28_%29.md)
  Accesses the element at the specified position.
### Type Aliases
- [KeyValuePairs.Element](./element.md)
  The element type of a `KeyValuePairs`: a tuple containing an individual key-value pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyvaluepairs/randomaccesscollection-implementations)*