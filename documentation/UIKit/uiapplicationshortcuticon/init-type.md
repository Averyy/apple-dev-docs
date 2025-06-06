# init(type:)

**Framework**: UIKit  
**Kind**: init

Creates a Home Screen quick action icon using a system-defined image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(type: UIApplicationShortcutIcon.IconType)
```

#### Return Value

A Home Screen quick action icon initialized with the specified system image.

#### Discussion

Use this method to create icons for actions supported by the system. Users expect system-defined action images to be used only for the intended action.

## Parameters

- `type`: The system-defined image to use for the icon. For a list of possible images, see the   enumeration.

## See Also

- [convenience init(templateImageName: String)](uiapplicationshortcuticon/init(templateimagename:).md)
  Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [convenience init(systemImageName: String)](uiapplicationshortcuticon/init(systemimagename:).md)
  Creates a Home Screen quick action icon using a system symbol image.
- [convenience init(contact: CNContact)](uiapplicationshortcuticon/init(contact:).md)
  Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(type:))*