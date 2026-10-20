# init(type:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) iconWithType:(UIApplicationShortcutIconType) type;
```

#### Return Value

A Home Screen quick action icon initialized with the specified system image.

#### Discussion

Use this method to create icons for actions supported by the system. Users expect system-defined action images to be used only for the intended action.

## Parameters

- `type`: The system-defined image to use for the icon. For a list of possible images, see the [`UIApplicationShortcutIcon.IconType`](./icontype.md) enumeration.

## See Also

### Creating a quick action icon
- [convenience init(templateImageName: String)](./init%28templateimagename%29.md)
  Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [convenience init(systemImageName: String)](./init%28systemimagename%29.md)
  Creates a Home Screen quick action icon using a system symbol image.
- [convenience init(contact: CNContact)](./init%28contact%29.md)
  Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(type:))*