# UIApplicationShortcutIcon

**Framework**: UIKit  
**Kind**: class

An image you can optionally associate with a Home Screen quick action to improve its appearance and usability.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class UIApplicationShortcutIcon
```

#### Overview

To associate an icon with a quick action, pass it to the quick action item’s initialization method, as described in [`UIApplicationShortcutItem`](uiapplicationshortcutitem.md).

There are three types of quick action icon:

- An icon from a system-provided library of common types, as described in the [`UIApplicationShortcutIcon.IconType`](uiapplicationshortcuticon/icontype.md) enumeration
- An icon derived from a custom template image in your app’s bundle and preferably in an asset catalog (see [`Managing assets with asset catalogs`](https://developer.apple.com/documentation/Xcode/managing-assets-with-asset-catalogs))
- An icon representing a contact in the user’s address book, which you access through the [`Contacts UI`](https://developer.apple.com/documentation/ContactsUI) framework

## Topics

### Creating a quick action icon
- [convenience init(type: UIApplicationShortcutIcon.IconType)](uiapplicationshortcuticon/init(type:).md)
  Creates a Home Screen quick action icon using a system-defined image.
- [convenience init(templateImageName: String)](uiapplicationshortcuticon/init(templateimagename:).md)
  Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [convenience init(systemImageName: String)](uiapplicationshortcuticon/init(systemimagename:).md)
  Creates a Home Screen quick action icon using a system symbol image.
- [convenience init(contact: CNContact)](uiapplicationshortcuticon/init(contact:).md)
  Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.
### Constants
- [UIApplicationShortcutIcon.IconType](uiapplicationshortcuticon/icontype.md)
  Constants for system-provided icons.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Add Home Screen quick actions](add-home-screen-quick-actions.md)
  Expose commonly used functionality with static or dynamic 3D Touch Home Screen quick actions.
- [class UIApplicationShortcutItem](uiapplicationshortcutitem.md)
  An application shortcut item, also called a Home Screen dynamic quick action, that specifies a user-initiated action for your app.
- [class UIMutableApplicationShortcutItem](uimutableapplicationshortcutitem.md)
  A mutable Home Screen dynamic quick action, which is an item that specifies a configurable user-initiated action for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon)*