# addSubgroup(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Adds a subgroup to another group.

**Availability**:
- macOS

## Declaration

```swift
func addSubgroup(_ group: ABGroup!) -> Bool
```

```objc
- (BOOL) addSubgroup:(ABGroup *) group;
```

## Return Value

[`true`](../../Swift/true.md) if successful; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the `group` argument is already part of the receiver, this method does nothing and returns [`false`](../../Swift/false.md). If adding the group would create a recursion, this method also does nothing and returns [`false`](../../Swift/false.md). (For example, if the group Animal Lovers is in Dog Lovers, and you add Dog Lovers to Animal Lovers, that would create a recursion, which this method won’t allow.) If the `group` argument is `nil`, this method raises an exception.

## Parameters

- `group`: The group to add as a subgroup.

## See Also

### Managing subgroups
- [func removeSubgroup(ABGroup!) -> Bool](./removesubgroup%28_%29.md)
  Removes a subgroup from a group.
- [func parentGroups() -> [Any]!](./parentgroups%28%29.md)
  Returns an array containing a group’s parents—that is, the groups that a group belongs to.
- [func subgroups() -> [Any]!](./subgroups%28%29.md)
  Returns an array containing a group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroup/addsubgroup(_:))*