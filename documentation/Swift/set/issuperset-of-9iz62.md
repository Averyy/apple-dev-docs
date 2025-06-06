# isSuperset(of:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value that indicates whether this set is a superset of the given set.

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
func isSuperset(of other: Set<Element>) -> Bool
```

#### Return Value

`true` if the set is a superset of `other`; otherwise, `false`.

#### Discussion

Set  is a superset of another set  if every member of  is also a member of .

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(employees.isSuperset(of: attendees))
// Prints "true"
```

## Parameters

- `other`: Another set.

## See Also

- [static func == (Set<Element>, Set<Element>) -> Bool](set/==(_:_:).md)
  Returns a Boolean value indicating whether two sets have equal elements.
- [static func != (Self, Self) -> Bool](set/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Set<Element>) -> Bool](set/issubset(of:)-1d7pp.md)
  Returns a Boolean value that indicates whether this set is a subset of the given set.
- [func isSubset<S>(of: S) -> Bool](set/issubset(of:)-6qyo5.md)
  Returns a Boolean value that indicates whether the set is a subset of the given sequence.
- [func isStrictSubset(of: Set<Element>) -> Bool](set/isstrictsubset(of:)-96vc3.md)
  Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [func isStrictSubset<S>(of: S) -> Bool](set/isstrictsubset(of:)-787sx.md)
  Returns a Boolean value that indicates whether the set is a strict subset of the given sequence.
- [func isSuperset<S>(of: S) -> Bool](set/issuperset(of:)-90hri.md)
  Returns a Boolean value that indicates whether the set is a superset of the given sequence.
- [func isStrictSuperset(of: Set<Element>) -> Bool](set/isstrictsuperset(of:)-4d27m.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isStrictSuperset<S>(of: S) -> Bool](set/isstrictsuperset(of:)-58ejg.md)
  Returns a Boolean value that indicates whether the set is a strict superset of the given sequence.
- [func isDisjoint(with: Set<Element>) -> Bool](set/isdisjoint(with:)-8ngmk.md)
  Returns a Boolean value that indicates whether this set has no members in common with the given set.
- [func isDisjoint<S>(with: S) -> Bool](set/isdisjoint(with:)-2onid.md)
  Returns a Boolean value that indicates whether the set has no members in common with the given sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/issuperset(of:)-9iz62)*