# isStrictSuperset(of:)

**Framework**: BrowserEngineKit  
**Kind**: method

Returns a Boolean value that indicates whether this set is a strict superset of the given set.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func isStrictSuperset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a strict superset of `other`; otherwise, `false`.

#### Discussion

Set  is a strict superset of another set  if every member of  is also a member of  and  contains at least one element that is  a member of .

```None
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

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beselectionflags/isstrictsuperset(of:))*