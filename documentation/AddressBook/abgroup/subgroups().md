# subgroups()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns an array containing a group’s subgroups.

**Availability**:
- macOS

## Declaration

```swift
func subgroups() -> [Any]!
```

```objc
- (NSArray *) subgroups;
```

#### Discussion

If this group doesn’t contain any groups, this method returns an empty array.

## See Also

### Managing subgroups
- [func addSubgroup(ABGroup!) -> Bool](./addsubgroup%28_%29.md)
  Adds a subgroup to another group.
- [func removeSubgroup(ABGroup!) -> Bool](./removesubgroup%28_%29.md)
  Removes a subgroup from a group.
- [func parentGroups() -> [Any]!](./parentgroups%28%29.md)
  Returns an array containing a group’s parents—that is, the groups that a group belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/subgroups())*