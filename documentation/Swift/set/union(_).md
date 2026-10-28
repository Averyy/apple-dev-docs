# union(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a new set with the elements of both this set and the given sequence.

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
func union<S>(_ other: S) -> Set<Element> where Element == S.Element, S : Sequence
```

Available when `Element` conforms to `Hashable`.

## Return Value

A new set with the unique elements of this set and `other`.

## Discussion

In the following example, the `attendeesAndVisitors` set is made up of the elements of the `attendees` set and the `visitors` array:

```swift
let attendees: Set = ["Alicia", "Bethany", "Diana"]
let visitors = ["Marcia", "Nathaniel"]
let attendeesAndVisitors = attendees.union(visitors)
print(attendeesAndVisitors)
// Prints "["Diana", "Nathaniel", "Bethany", "Alicia", "Marcia"]"
```

If the set already contains one or more elements that are also in `other`, the existing members are kept. If `other` contains multiple instances of equivalent elements, only the first instance is kept.

```swift
let initialIndices = Set(0..<5)
let expandedIndices = initialIndices.union([2, 3, 6, 6, 7, 7])
print(expandedIndices)
// Prints "[2, 4, 6, 7, 0, 1, 3]"
```

## Parameters

- `other`: A sequence of elements. `other` must be finite.

## See Also

### Combining Sets
- [func formUnion<S>(S)](./formunion%28_%29.md)
  Inserts the elements of the given sequence into the set.
- [func intersection(Set<Element>) -> Set<Element>](./intersection%28_%29-1zh8f.md)
  Returns a new set with the elements that are common to both this set and the given sequence.
- [func intersection<S>(S) -> Set<Element>](./intersection%28_%29-6uts9.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/union(_:))*