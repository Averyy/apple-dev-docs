# isSubset(of:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether the set is a subset of another set.

**Availability**:
- iOS ?+
- iPadOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func isSubset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a subset of `other`; otherwise, `false`.

#### Discussion

Set  is a subset of another set  if every member of  is also a member of .

```None
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(attendees.isSubset(of: employees))
// Prints "true"
```

## Parameters

- `other`: A set of the same type as the current set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectedge/issubset(of:))*