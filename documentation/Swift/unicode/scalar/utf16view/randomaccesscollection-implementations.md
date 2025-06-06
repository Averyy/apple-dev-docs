# RandomAccessCollection Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var endIndex: Int](unicode/scalar/utf16view/endindex.md)
  The “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: Int](unicode/scalar/utf16view/startindex.md)
  The position of the first code unit.
### Instance Methods
- [func index(Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Self.Index?](unicode/scalar/utf16view/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
### Subscripts
- [subscript(Int) -> UTF16.CodeUnit](unicode/scalar/utf16view/subscript(_:).md)
  Accesses the code unit at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/utf16view/randomaccesscollection-implementations)*