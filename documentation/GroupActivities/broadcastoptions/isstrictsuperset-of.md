# isStrictSuperset(of:)

**Framework**: Group Activities  
**Kind**: method

Returns a Boolean value that indicates whether this set is a strict superset of the given set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func isStrictSuperset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a strict superset of `other`; otherwise, `false`.

#### Discussion

Set  is a strict superset of another set  if every member of  is also a member of  and  contains at least one element that is  a member of .

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

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/broadcastoptions/isstrictsuperset(of:))*