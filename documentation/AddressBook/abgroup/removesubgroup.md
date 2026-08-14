# removeSubgroup(_:)

**Framework**: Address Book  
**Kind**: method

Removes a subgroup from a group.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeSubgroup(_ group: ABGroup!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the `group` argument is not a subgroup, this method does nothing and returns [`false`](https://developer.apple.com/documentation/swift/false). If `group` is `nil`, this method raises an exception.

## Parameters

- `group`: The subgroup to be removed.

## See Also

- [func addSubgroup(ABGroup!) -> Bool](abgroup/addsubgroup(_:).md)
  Adds a subgroup to another group.
- [func parentGroups() -> [Any]!](abgroup/parentgroups.md)
  Returns an array containing a group’s parents—that is, the groups that a group belongs to.
- [func subgroups() -> [Any]!](abgroup/subgroups.md)
  Returns an array containing a group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/removesubgroup(_:))*