# init(templateImageName:)

**Framework**: UIKit  
**Kind**: init

Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(templateImageName: String)
```

#### Return Value

A Home Screen quick action icon initialized with the specified template image provided by your app.

#### Discussion

Use this method to create icons based on custom artwork that you provide. If the image name you specify doesn’t correspond to a valid image resource in your app bundle, the system won’t display an icon.

For more information about designing custom images, see [`Providing images for different appearances`](providing-images-for-different-appearances.md).

## Parameters

- `templateImageName`: The name of a custom image in the app’s asset catalog. If the image isn’t in your app’s asset catalog, this method searches the app bundle for the image. You don’t need to specify the filename extension or the `@2x` or `@3x` modifiers for this name. This method retrieves the appropriate image based on the system and the available image resources.

## See Also

- [convenience init(type: UIApplicationShortcutIcon.IconType)](uiapplicationshortcuticon/init(type:).md)
  Creates a Home Screen quick action icon using a system-defined image.
- [convenience init(systemImageName: String)](uiapplicationshortcuticon/init(systemimagename:).md)
  Creates a Home Screen quick action icon using a system symbol image.
- [convenience init(contact: CNContact)](uiapplicationshortcuticon/init(contact:).md)
  Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(templateimagename:))*