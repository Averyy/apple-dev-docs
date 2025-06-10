# parentGroups()

**Framework**: Address Book  
**Kind**: method

Returns an array containing a group’s parents—that is, the groups that a group belongs to.

**Availability**:
- macOS ?+

## Declaration

```swift
func parentGroups() -> [Any]!
```

#### Discussion

If this group doesn’t belong to any groups, this method returns an empty array.

## See Also

- [func addSubgroup(ABGroup!) -> Bool](abgroup/addsubgroup(_:).md)
  Adds a subgroup to another group.
- [func removeSubgroup(ABGroup!) -> Bool](abgroup/removesubgroup(_:).md)
  Removes a subgroup from a group.
- [func subgroups() -> [Any]!](abgroup/subgroups.md)
  Returns an array containing a group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/parentgroups())*