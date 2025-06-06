# removeSubgroup(_:from:)

**Framework**: Contacts  
**Kind**: method

Remove a subgroup from the specified parent group.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func removeSubgroup(_ subgroup: CNGroup, from group: CNGroup)
```

#### Discussion

If you previously tried to add `subgroup` to `group` in the same save request, calling this method undoes that addition. The last change you make is the one that takes effect.

## Parameters

- `subgroup`: The subgroup to remove.
- `group`: The parent group containing  .

## See Also

- [func addSubgroup(CNGroup, to: CNGroup)](cnsaverequest/addsubgroup(_:to:).md)
  Add the specified group to a parent group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/removesubgroup(_:from:))*