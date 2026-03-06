# isStrictSuperset(of:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value that indicates whether this set is a strict superset of the given set.

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
func isStrictSuperset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a strict superset of `other`; otherwise, `false`.

#### Discussion

Set *A* is a strict superset of another set *B* if every member of *B* is also a member of *A* and *A* contains at least one element that is *not* a member of *B*.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(employees.isStrictSuperset(of: attendees))
// Prints "true"

// A set is never a strict superset of itself:
print(employees.isStrictSuperset(of: employees))
// Prints "false"
```

## Parameters

- `other`: A set of the same type as the current set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clocktraits/isstrictsuperset(of:))*