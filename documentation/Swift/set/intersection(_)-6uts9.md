# intersection(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a new set with the elements that are common to both this set and the given sequence.

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
func intersection<S>(_ other: S) -> Set<Element> where Element == S.Element, S : Sequence
```

Available when `Element` conforms to `Hashable`.

## Return Value

A new set.

## Discussion

In the following example, the `bothNeighborsAndEmployees` set is made up of the elements that are in *both* the `employees` and `neighbors` sets. Elements that are in only one or the other are left out of the result of the intersection.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors = ["Bethany", "Eric", "Forlani", "Greta"]
let bothNeighborsAndEmployees = employees.intersection(neighbors)
print(bothNeighborsAndEmployees)
// Prints "["Bethany", "Eric"]"
```

## Parameters

- `other`: A sequence of elements. `other` must be finite.

## See Also

### Combining Sets
- [func union<S>(S) -> Set<Element>](./union%28_%29.md)
  Returns a new set with the elements of both this set and the given sequence.
- [func formUnion<S>(S)](./formunion%28_%29.md)
  Inserts the elements of the given sequence into the set.
- [func intersection(Set<Element>) -> Set<Element>](./intersection%28_%29-1zh8f.md)
  Returns a new set with the elements that are common to both this set and the given sequence.
- [func formIntersection<S>(S)](./formintersection%28_%29.md)
  Removes the elements of the set that aren’t also in the given sequence.
- [func symmetricDifference<S>(S) -> Set<Element>](./symmetricdifference%28_%29.md)
  Returns a new set with the elements that are either in this set or in the given sequence, but not in both.
- [func formSymmetricDifference(Set<Element>)](./formsymmetricdifference%28_%29-22p0m.md)
  Removes the elements of the set that are also in the given sequence and adds the members of the sequence that are not already in the set.
- [func formSymmetricDifference<S>(S)](./formsymmetricdifference%28_%29-5u38b.md)
  Replace this set with the elements contained in this set or the given set, but not both.
- [func subtract(Set<Element>)](./subtract%28_%29-8gc48.md)
  Removes the elements of the given set from this set.
- [func subtract<S>(S)](./subtract%28_%29-7cd3y.md)
  Removes the elements of the given sequence from the set.
- [func subtracting(Set<Element>) -> Set<Element>](./subtracting%28_%29-3n4lc.md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func subtracting<S>(S) -> Set<Element>](./subtracting%28_%29-2qge3.md)
  Returns a new set containing the elements of this set that do not occur in the given sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/intersection(_:)-6uts9)*