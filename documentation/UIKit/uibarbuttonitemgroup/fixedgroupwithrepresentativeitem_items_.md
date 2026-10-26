# fixedGroupWithRepresentativeItem:items:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
+ (UIBarButtonItemGroup *) fixedGroupWithRepresentativeItem:(UIBarButtonItem *) representativeItem items:(NSArray<UIBarButtonItem *> *) items;
```

## Parameters

- `representativeItem`: The item to display for the group when space is constrained.
- `items`: The items to include in the group.

## See Also

### Creating a group
- [+ movableGroupWithCustomizationIdentifier:representativeItem:items:](./movablegroupwithcustomizationidentifier_representativeitem_items_.md)
  Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [+ optionalGroupWithCustomizationIdentifier:inDefaultCustomization:representativeItem:items:](./optionalgroupwithcustomizationidentifier_indefaultcustomization_representativeitem_items_.md)
  Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [init(barButtonItems: [UIBarButtonItem], representativeItem: UIBarButtonItem?)](./init%28barbuttonitems,representativeitem%29.md)
  Creates a fixed group with the specified items.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a bar button item group from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/fixedgroupwithrepresentativeitem:items:)*