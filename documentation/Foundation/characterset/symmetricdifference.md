# symmetricDifference(_:)

**Framework**: Foundation  
**Kind**: method

Returns an exclusive or of the `CharacterSet` with another `CharacterSet`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func symmetricDifference(_ other: CharacterSet) -> CharacterSet
```

## See Also

- [func formIntersection(CharacterSet)](characterset/formintersection(_:).md)
  Sets the value to an intersection of the `CharacterSet` with another `CharacterSet`.
- [func formSymmetricDifference(CharacterSet)](characterset/formsymmetricdifference(_:).md)
  Sets the value to an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [func formUnion(CharacterSet)](characterset/formunion(_:).md)
  Sets the value to a union of the `CharacterSet` with another `CharacterSet`.
- [func hasMember(inPlane: UInt8) -> Bool](characterset/hasmember(inplane:).md)
  Returns true if the `CharacterSet` has a member in the specified plane.
- [func insert(charactersIn: String)](characterset/insert(charactersin:)-2syuj.md)
  Insert the values from the specified string into the `CharacterSet`.
- [func intersection(CharacterSet) -> CharacterSet](characterset/intersection(_:).md)
  Returns an intersection of the `CharacterSet` with another `CharacterSet`.
- [func invert()](characterset/invert.md)
  Invert the contents of the `CharacterSet`.
- [func isSuperset(of: CharacterSet) -> Bool](characterset/issuperset(of:).md)
  Returns true if `self` is a superset of `other`.
- [func remove(charactersIn: String)](characterset/remove(charactersin:)-3sayw.md)
  Remove the values from the specified string from the `CharacterSet`.
- [func subtracting(CharacterSet) -> CharacterSet](characterset/subtracting(_:).md)
  Returns a `CharacterSet` created by removing elements in `other` from `self`.
- [func union(CharacterSet) -> CharacterSet](characterset/union(_:).md)
  Returns a union of the `CharacterSet` with another `CharacterSet`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/characterset/symmetricdifference(_:))*