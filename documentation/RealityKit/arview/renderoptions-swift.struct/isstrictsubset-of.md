# isStrictSubset(of:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value that indicates whether this set is a strict subset of the given set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
func isStrictSubset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a strict subset of `other`; otherwise, `false`.

#### Discussion

Set  is a strict subset of another set  if every member of  is also a member of  and  contains at least one element that is not a member of .

```None
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(attendees.isStrictSubset(of: employees))
// Prints "true"

// A set is never a strict subset of itself:
print(attendees.isStrictSubset(of: attendees))
// Prints "false"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [static func != (Self, Self) -> Bool](arview/renderoptions-swift.struct/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Self) -> Bool](arview/renderoptions-swift.struct/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](arview/renderoptions-swift.struct/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](arview/renderoptions-swift.struct/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isDisjoint(with: Self) -> Bool](arview/renderoptions-swift.struct/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/isstrictsubset(of:))*