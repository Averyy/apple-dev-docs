# hasMember(inPlane:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns true if the `CharacterSet` has a member in the specified plane.

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
func hasMember(inPlane plane: UInt8) -> Bool
```

## Discussion

This method makes it easier to find the plane containing the members of the current character set. The Basic Multilingual Plane (BMP) is plane 0.

## See Also

### Combining Character Sets
- [func formIntersection(CharacterSet)](./formintersection%28_%29.md)
  Sets the value to an intersection of the `CharacterSet` with another `CharacterSet`.
- [func formSymmetricDifference(CharacterSet)](./formsymmetricdifference%28_%29.md)
  Sets the value to an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [func formUnion(CharacterSet)](./formunion%28_%29.md)
  Sets the value to a union of the `CharacterSet` with another `CharacterSet`.
- [func insert(charactersIn: String)](./insert%28charactersin%29-2syuj.md)
  Insert the values from the specified string into the `CharacterSet`.
- [func intersection(CharacterSet) -> CharacterSet](./intersection%28_%29.md)
  Returns an intersection of the `CharacterSet` with another `CharacterSet`.
- [func invert()](./invert%28%29.md)
  Invert the contents of the `CharacterSet`.
- [func isSuperset(of: CharacterSet) -> Bool](./issuperset%28of%29.md)
  Returns true if `self` is a superset of `other`.
- [func remove(charactersIn: String)](./remove%28charactersin%29-3sayw.md)
  Remove the values from the specified string from the `CharacterSet`.
- [func subtracting(CharacterSet) -> CharacterSet](./subtracting%28_%29.md)
  Returns a `CharacterSet` created by removing elements in `other` from `self`.
- [func symmetricDifference(CharacterSet) -> CharacterSet](./symmetricdifference%28_%29.md)
  Returns an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [func union(CharacterSet) -> CharacterSet](./union%28_%29.md)
  Returns a union of the `CharacterSet` with another `CharacterSet`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/characterset/hasmember(inplane:))*