# creatingOptionalGroup(customizationIdentifier:isInDefaultCustomization:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Places the item in an optional group that a person can move, add to, or remove from the navigation bar during layout customization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func creatingOptionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool = true) -> UIBarButtonItemGroup
```

## Return Value

A [`UIBarButtonItemGroup`](../uibarbuttonitemgroup.md) that contains only this bar button item.

## Discussion

A bar button item can only belong to one [`UIBarButtonItemGroup`](../uibarbuttonitemgroup.md). If you add a bar button item to a new group, the system removes it from its previous group.

## Parameters

- `customizationIdentifier`: A unique string to identify the group for navigation bar layout customization.
- `isInDefaultCustomization`: A Boolean that determines whether to place the group in the navigation bar by default. Specify [`false`](../../Swift/false.md) if you want the group to appear in the navigation bar customization popover by default.

## See Also

### Creating groups
- [func creatingFixedGroup() -> UIBarButtonItemGroup](./creatingfixedgroup%28%29.md)
  Places the item in a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [func creatingMovableGroup(customizationIdentifier: String) -> UIBarButtonItemGroup](./creatingmovablegroup%28customizationidentifier%29.md)
  Places the item in a movable group that a person can move but can’t remove from the navigation bar during layout customization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/creatingoptionalgroup(customizationidentifier:isindefaultcustomization:))*