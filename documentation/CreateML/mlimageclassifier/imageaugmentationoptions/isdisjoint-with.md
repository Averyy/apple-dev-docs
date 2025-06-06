# isDisjoint(with:)

**Framework**: Create ML  
**Kind**: method

Returns a Boolean value that indicates whether the set has no members in common with the given set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func isDisjoint(with other: Self) -> Bool
```

#### Return Value

`true` if the set has no elements in common with `other`; otherwise, `false`.

#### Discussion

In the following example, the `employees` set is disjoint with the `visitors` set because no name appears in both sets.

```None
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let visitors: Set = ["Marcia", "Nathaniel", "Olivia"]
print(employees.isDisjoint(with: visitors))
// Prints "true"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [func isStrictSubset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSubset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSuperset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSuperset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/isdisjoint(with:))*