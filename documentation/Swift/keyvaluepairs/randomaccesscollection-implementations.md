# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: KeyValuePairs<Key, Value>.Index](keyvaluepairs/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: KeyValuePairs<Key, Value>.Index](keyvaluepairs/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](keyvaluepairs/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
### Subscripts
- [subscript(KeyValuePairs<Key, Value>.Index) -> KeyValuePairs<Key, Value>.Element](keyvaluepairs/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [KeyValuePairs.Element](keyvaluepairs/element.md)
  The element type of a `KeyValuePairs`: a tuple containing an individual key-value pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyvaluepairs/randomaccesscollection-implementations)*