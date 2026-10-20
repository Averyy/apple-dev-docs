# optionalGroup(customizationIdentifier:isInDefaultCustomization:representativeItem:items:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency class func optionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool = true, representativeItem: UIBarButtonItem? = nil, items: [UIBarButtonItem]) -> UIBarButtonItemGroup
```

## Parameters

- `customizationIdentifier`: A unique string to identify the group for navigation bar layout customization.
- `isInDefaultCustomization`: A Boolean that determines whether to place the group in the navigation bar by default. Specify [`false`](../../Swift/false.md) if you want the group to appear in the navigation bar customization popover by default.
- `representativeItem`: The item to display for the group when space is constrained.
- `items`: The items to include in the group.

## See Also

### Creating a group
- [class func fixedGroup(representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](./fixedgroup%28representativeitem,items%29.md)
  Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [class func movableGroup(customizationIdentifier: String, representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](./movablegroup%28customizationidentifier,representativeitem,items%29.md)
  Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [init(barButtonItems: [UIBarButtonItem], representativeItem: UIBarButtonItem?)](./init%28barbuttonitems,representativeitem%29.md)
  Creates a fixed group with the specified items.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a bar button item group from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/optionalgroup(customizationidentifier:isindefaultcustomization:representativeitem:items:))*