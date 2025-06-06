# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Repeated<Element>.Index](repeated/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Repeated<Element>.Index](repeated/startindex.md)
  The position of the first element in a nonempty collection.
### Instance Methods
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](repeated/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
### Subscripts
- [subscript(Int) -> Element](repeated/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [typealias Index](repeated/index.md)
  A type that represents a valid position in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/repeated/randomaccesscollection-implementations)*