# isSuperset(of:)

**Framework**: MusicKit  
**Kind**: method

Returns a Boolean value that indicates whether the set is a superset of the given set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musictokenrequestoptions/issuperset(of:))*