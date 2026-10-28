# removeSubgroup(_:from:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Remove a subgroup from the specified parent group.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func removeSubgroup(_ subgroup: CNGroup, from group: CNGroup)
```

```objc
- (void) removeSubgroup:(CNGroup *) subgroup fromGroup:(CNGroup *) group;
```

## Discussion

If you previously tried to add `subgroup` to `group` in the same save request, calling this method undoes that addition. The last change you make is the one that takes effect.

## Parameters

- `subgroup`: The subgroup to remove.
- `group`: The parent group containing `subgroup`.

## See Also

### Adding and removing subgroups
- [func addSubgroup(CNGroup, to: CNGroup)](./addsubgroup%28_,to%29.md)
  Add the specified group to a parent group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/removesubgroup(_:from:))*