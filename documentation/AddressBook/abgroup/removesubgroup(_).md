# removeSubgroup(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Removes a subgroup from a group.

**Availability**:
- macOS

## Declaration

```swift
func removeSubgroup(_ group: ABGroup!) -> Bool
```

```objc
- (BOOL) removeSubgroup:(ABGroup *) group;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; otherwise, [`false`](../../Swift/false.md).

#### Discussion

If the `group` argument is not a subgroup, this method does nothing and returns [`false`](../../Swift/false.md). If `group` is `nil`, this method raises an exception.

## Parameters

- `group`: The subgroup to be removed.

## See Also

### Managing subgroups
- [func addSubgroup(ABGroup!) -> Bool](./addsubgroup%28_%29.md)
  Adds a subgroup to another group.
- [func parentGroups() -> [Any]!](./parentgroups%28%29.md)
  Returns an array containing a group’s parents—that is, the groups that a group belongs to.
- [func subgroups() -> [Any]!](./subgroups%28%29.md)
  Returns an array containing a group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/removesubgroup(_:))*