# subtracting(_:)

**Framework**: Swift  
**Kind**: method

Returns a new set containing the elements of this set that do not occur in the given sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func subtracting<S>(_ other: S) -> Set<Element> where Element == S.Element, S : Sequence
```

#### Return Value

A new set.

#### Discussion

In the following example, the `nonNeighbors` set is made up of the elements of the `employees` set that are not elements of `neighbors`:

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors = ["Bethany", "Eric", "Forlani", "Greta"]
let nonNeighbors = employees.subtracting(neighbors)
print(nonNeighbors)
// Prints "["Chris", "Diana", "Alicia"]"
```

## Parameters

- `other`: A sequence of elements.   must be finite.

## See Also

- [func union<S>(S) -> Set<Element>](set/union(_:).md)
  Returns a new set with the elements of both this set and the given sequence.
- [func formUnion<S>(S)](set/formunion(_:).md)
  Inserts the elements of the given sequence into the set.
- [func intersection(Set<Element>) -> Set<Element>](set/intersection(_:)-1zh8f.md)
  Returns a new set with the elements that are common to both this set and the given sequence.
- [func intersection<S>(S) -> Set<Element>](set/intersection(_:)-6uts9.md)
  Returns a new set with the elements that are common to both this set and the given sequence.
- [func formIntersection<S>(S)](set/formintersection(_:).md)
  Removes the elements of the set that aren’t also in the given sequence.
- [func symmetricDifference<S>(S) -> Set<Element>](set/symmetricdifference(_:).md)
  Returns a new set with the elements that are either in this set or in the given sequence, but not in both.
- [func formSymmetricDifference(Set<Element>)](set/formsymmetricdifference(_:)-22p0m.md)
  Removes the elements of the set that are also in the given sequence and adds the members of the sequence that are not already in the set.
- [func formSymmetricDifference<S>(S)](set/formsymmetricdifference(_:)-5u38b.md)
  Replace this set with the elements contained in this set or the given set, but not both.
- [func subtract(Set<Element>)](set/subtract(_:)-8gc48.md)
  Removes the elements of the given set from this set.
- [func subtract<S>(S)](set/subtract(_:)-7cd3y.md)
  Removes the elements of the given sequence from the set.
- [func subtracting(Set<Element>) -> Set<Element>](set/subtracting(_:)-3n4lc.md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/subtracting(_:)-2qge3)*