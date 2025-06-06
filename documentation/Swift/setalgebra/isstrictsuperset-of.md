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

## See Also

- [func isStrictSubset(of: Self) -> Bool](setalgebra/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/isstrictsuperset(of:))*