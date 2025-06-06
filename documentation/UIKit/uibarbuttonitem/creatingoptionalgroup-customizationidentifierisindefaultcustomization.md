# creatingOptionalGroup(customizationIdentifier:isInDefaultCustomization:)

**Framework**: UIKit  
**Kind**: method

Places the item in an optional group that a person can move, add to, or remove from the navigation bar during layout customization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func creatingOptionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool = true) -> UIBarButtonItemGroup
```

#### Return Value

A [`UIBarButtonItemGroup`](uibarbuttonitemgroup.md) that contains only this bar button item.

#### Discussion

A bar button item can only belong to one [`UIBarButtonItemGroup`](uibarbuttonitemgroup.md). If you add a bar button item to a new group, the system removes it from its previous group.

## Parameters

- `customizationIdentifier`: A unique string to identify the group for navigation bar layout customization.
- `isInDefaultCustomization`: A Boolean that determines whether to place the group in the navigation bar by default. Specify   if you want the group to appear in the navigation bar customization popover by default.

## See Also

- [func creatingFixedGroup() -> UIBarButtonItemGroup](uibarbuttonitem/creatingfixedgroup.md)
  Places the item in a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [func creatingMovableGroup(customizationIdentifier: String) -> UIBarButtonItemGroup](uibarbuttonitem/creatingmovablegroup(customizationidentifier:).md)
  Places the item in a movable group that a person can move but can’t remove from the navigation bar during layout customization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/creatingoptionalgroup(customizationidentifier:isindefaultcustomization:))*