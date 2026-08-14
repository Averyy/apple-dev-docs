# addSubgroup(_:)

**Framework**: Address Book  
**Kind**: method

Adds a subgroup to another group.

**Availability**:
- macOS ?+

## Declaration

```swift
func addSubgroup(_ group: ABGroup!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the `group` argument is already part of the receiver, this method does nothing and returns [`false`](https://developer.apple.com/documentation/swift/false). If adding the group would create a recursion, this method also does nothing and returns [`false`](https://developer.apple.com/documentation/swift/false). (For example, if the group Animal Lovers is in Dog Lovers, and you add Dog Lovers to Animal Lovers, that would create a recursion, which this method won’t allow.) If the `group` argument is `nil`, this method raises an exception.

## Parameters

- `group`: The group to add as a subgroup.

## See Also

- [func removeSubgroup(ABGroup!) -> Bool](abgroup/removesubgroup(_:).md)
  Removes a subgroup from a group.
- [func parentGroups() -> [Any]!](abgroup/parentgroups.md)
  Returns an array containing a group’s parents—that is, the groups that a group belongs to.
- [func subgroups() -> [Any]!](abgroup/subgroups.md)
  Returns an array containing a group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/addsubgroup(_:))*