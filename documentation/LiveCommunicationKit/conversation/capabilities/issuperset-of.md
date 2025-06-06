# isSuperset(of:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Returns a Boolean value that indicates whether the set is a superset of the given set.

## Declaration

```swift
func isSuperset(of other: Self) -> Bool
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

- `other`: A set of the same type as the current set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/capabilities/issuperset(of:))*