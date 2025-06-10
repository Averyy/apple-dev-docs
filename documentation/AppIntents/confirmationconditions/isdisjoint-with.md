# isDisjoint(with:)

**Framework**: App Intents  
**Kind**: method

Returns a Boolean value that indicates whether the set has no members in common with the given set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func isDisjoint(with other: Self) -> Bool
```

#### Return Value

`true` if the set has no elements in common with `other`; otherwise, `false`.

#### Discussion

In the following example, the `employees` set is disjoint with the `visitors` set because no name appears in both sets.

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let visitors: Set = ["Marcia", "Nathaniel", "Olivia"]
print(employees.isDisjoint(with: visitors))
// Prints "true"
```

## Parameters

- `other`: A set of the same type as the current set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/confirmationconditions/isdisjoint(with:))*