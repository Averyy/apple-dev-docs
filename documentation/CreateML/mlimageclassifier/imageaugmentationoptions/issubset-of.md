# isSubset(of:)

**Framework**: Create ML  
**Kind**: method

Returns a Boolean value that indicates whether the set is a subset of another set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

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

## See Also

- [func isStrictSubset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSuperset(of: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isDisjoint(with: Self) -> Bool](mlimageclassifier/imageaugmentationoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/issubset(of:))*