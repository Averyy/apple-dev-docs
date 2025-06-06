# init(coder:)

**Framework**: UIKit  
**Kind**: init

Creates a bar button item group from data in an unarchiver.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

## See Also

- [class func fixedGroup(representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](uibarbuttonitemgroup/fixedgroup(representativeitem:items:).md)
  Creates a fixed group that a person can’t move or remove from the navigation bar during layout customization.
- [class func movableGroup(customizationIdentifier: String, representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](uibarbuttonitemgroup/movablegroup(customizationidentifier:representativeitem:items:).md)
  Creates a movable group that a person can move but can’t remove from the navigation bar during layout customization.
- [class func optionalGroup(customizationIdentifier: String, isInDefaultCustomization: Bool, representativeItem: UIBarButtonItem?, items: [UIBarButtonItem]) -> UIBarButtonItemGroup](uibarbuttonitemgroup/optionalgroup(customizationidentifier:isindefaultcustomization:representativeitem:items:).md)
  Creates an optional group that a person can move, add to, or remove from the navigation bar during layout customization.
- [init(barButtonItems: [UIBarButtonItem], representativeItem: UIBarButtonItem?)](uibarbuttonitemgroup/init(barbuttonitems:representativeitem:).md)
  Creates a fixed group with the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/init(coder:))*