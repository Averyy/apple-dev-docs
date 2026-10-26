# init(barButtonItems:representativeItem:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a fixed group with the specified items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(barButtonItems: [UIBarButtonItem], representativeItem: UIBarButtonItem?)
```

```objc
- (instancetype) initWithBarButtonItems:(NSArray<UIBarButtonItem *> *) barButtonItems representativeItem:(UIBarButtonItem *) representativeItem;
```

#### Return Value

An initialized bar button item group.

#### Discussion

When you use this initializer to create a group for a navigation bar, it produces the same result as [`fixedGroup(representativeItem:items:)`](./fixedgroup%28representativeitem,items%29.md) (Swift) or [`fixedGroupWithRepresentativeItem:items:`](./fixedgroupwithrepresentativeitem_items_.md) (Objective-C).

When you use this initializer to create a group for the shortcuts bar, use the resulting group object to configure the [`leadingBarButtonGroups`](../uitextinputassistantitem/leadingbarbuttongroups.md) or [`trailingBarButtonGroups`](../uitextinputassistantitem/trailingbarbuttongroups.md) property of a [`UITextInputAssistantItem`](../uitextinputassistantitem.md) object.

## Parameters

- `barButtonItems`: The bar button items to display on the bar. Typically, the items in a group are related to each other in some way, although that need not be the case. You must not specify an empty array.
- `representativeItem`: A bar button item to display when there isn’t enough room to display the items in `barButtonItems`. The object you specify must be distinct from the objects in the `barButtonItems` parameter. It’s a programmer error to specify an object that’s also in the array passed to the `barButtonItems` parameter. You may specify `nil` for this parameter.

## See Also

### Creating a group
- [class func fixedGroup(representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](./fixedgroup%28representativeitem,items%29.md)
  Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [class func movableGroup(customizationIdentifier: String, representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](./movablegroup%28customizationidentifier,representativeitem,items%29.md)
  Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [class func optionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool, representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](./optionalgroup%28customizationidentifier,isindefaultcustomization,representativeitem,items%29.md)
  Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a bar button item group from data in an unarchiver.
- [+ fixedGroupWithRepresentativeItem:items:](./fixedgroupwithrepresentativeitem_items_.md)
  Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [+ movableGroupWithCustomizationIdentifier:representativeItem:items:](./movablegroupwithcustomizationidentifier_representativeitem_items_.md)
  Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [+ optionalGroupWithCustomizationIdentifier:inDefaultCustomization:representativeItem:items:](./optionalgroupwithcustomizationidentifier_indefaultcustomization_representativeitem_items_.md)
  Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/init(barbuttonitems:representativeitem:))*