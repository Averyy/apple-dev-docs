# isStrictSubset(of:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.

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
func isStrictSubset(of other: Set<Element>) -> Bool
```

Available when `Element` conforms to `Hashable`.

#### Return Value

`true` if the set is a strict subset of `other`; otherwise, `false`.

#### Discussion

Set *A* is a strict subset of another set *B* if every member of *A* is also a member of *B* and *B* contains at least one element that is not a member of *A*.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(attendees.isStrictSubset(of: employees))
// Prints "true"

// A set is never a strict subset of itself:
print(attendees.isStrictSubset(of: attendees))
// Prints "false"
```

## Parameters

- `other`: Another set.

## See Also

### Comparing Sets
- [static func == (Set<Element>, Set<Element>) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two sets have equal elements.
- [static func != (borrowing Self, borrowing Self) -> Bool](./noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Set<Element>) -> Bool](./issubset%28of%29-1d7pp.md)
  Returns a Boolean value that indicates whether this set is a subset of the given set.
- [func isSubset<S>(of: S) -> Bool](./issubset%28of%29-6qyo5.md)
  Returns a Boolean value that indicates whether the set is a subset of the given sequence.
- [func isStrictSubset<S>(of: S) -> Bool](./isstrictsubset%28of%29-787sx.md)
  Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [func isSuperset(of: Set<Element>) -> Bool](./issuperset%28of%29-9iz62.md)
  Returns a Boolean value that indicates whether this set is a superset of the given set.
- [func isSuperset<S>(of: S) -> Bool](./issuperset%28of%29-90hri.md)
  Returns a Boolean value that indicates whether the set is a superset of the given sequence.
- [func isStrictSuperset(of: Set<Element>) -> Bool](./isstrictsuperset%28of%29-4d27m.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isStrictSuperset<S>(of: S) -> Bool](./isstrictsuperset%28of%29-58ejg.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isDisjoint(with: Set<Element>) -> Bool](./isdisjoint%28with%29-8ngmk.md)
  Returns a Boolean value that indicates whether this set has no members in common with the given set.
- [func isDisjoint<S>(with: S) -> Bool](./isdisjoint%28with%29-2onid.md)
  Returns a Boolean value that indicates whether the set has no members in common with the given sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/isstrictsubset(of:)-96vc3)*