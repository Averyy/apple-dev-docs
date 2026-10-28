# addSubgroup(_:to:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Add the specified group to a parent group.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func addSubgroup(_ subgroup: CNGroup, to group: CNGroup)
```

```objc
- (void) addSubgroup:(CNGroup *) subgroup toGroup:(CNGroup *) group;
```

## Discussion

If you previously tried to remove `subgroup` from `group` in the same save request, calling this method undoes that removal. The last change you make is the one that takes effect.

## Parameters

- `subgroup`: The subgroup to add.
- `group`: The parent group in which to add `subgroup`.

## See Also

### Adding and removing subgroups
- [func removeSubgroup(CNGroup, from: CNGroup)](./removesubgroup%28_,from%29.md)
  Remove a subgroup from the specified parent group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/addsubgroup(_:to:))*