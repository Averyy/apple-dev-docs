# parentGroups()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns an array containing a group’s parents—that is, the groups that a group belongs to.

**Availability**:
- macOS

## Declaration

```swift
func parentGroups() -> [Any]!
```

```objc
- (NSArray *) parentGroups;
```

## Discussion

If this group doesn’t belong to any groups, this method returns an empty array.

## See Also

### Managing subgroups
- [func addSubgroup(ABGroup!) -> Bool](./addsubgroup%28_%29.md)
  Adds a subgroup to another group.
- [func removeSubgroup(ABGroup!) -> Bool](./removesubgroup%28_%29.md)
  Removes a subgroup from a group.
- [func subgroups() -> [Any]!](./subgroups%28%29.md)
  Returns an array containing a group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/parentgroups())*