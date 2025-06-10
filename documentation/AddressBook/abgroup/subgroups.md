# subgroups()

**Framework**: Address Book  
**Kind**: method

Returns an array containing a group’s subgroups.

**Availability**:
- macOS ?+

## Declaration

```swift
func subgroups() -> [Any]!
```

#### Discussion

If this group doesn’t contain any groups, this method returns an empty array.

## See Also

- [func addSubgroup(ABGroup!) -> Bool](abgroup/addsubgroup(_:).md)
  Adds a subgroup to another group.
- [func removeSubgroup(ABGroup!) -> Bool](abgroup/removesubgroup(_:).md)
  Removes a subgroup from a group.
- [func parentGroups() -> [Any]!](abgroup/parentgroups.md)
  Returns an array containing a group’s parents—that is, the groups that a group belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/subgroups())*