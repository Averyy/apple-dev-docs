# init(contact:)

**Framework**: Uikit  
**Kind**: init

Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(contact: CNContact)
```

#### Return Value

A Home Screen quick action icon initialized with the contact’s picture or monogram.

#### Discussion

To use this method, pass in a contact from the user’s contacts database, available through the [`CNContactStore`](https://developer.apple.com/documentation/Contacts/CNContactStore) object. If the contact you specify has a picture, the system creates a full-color quick action icon from that picture. If the contact has no picture, the system employs the contact’s initials and displays instead a monogram.

> **Note**:  This method employs the [`Contacts`](https://developer.apple.com/documentation/Contacts) framework.

You can, alternatively, pass in a [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) object you create at runtime. Such a contact must have at least a first name or a last name. The quick action icon returned from this method is then a monogram built from the contact’s name. With this approach, it isn’t possible for you to provide an image for the quick action icon.

Finally, you can call this method with an empty contact that you create by using the [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) class’s inherited [`alloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571958-alloc) and `init` methods. With this approach, the resulting icon is a monochrome silhouette.

When providing a set of contact quick actions, ensure that every one of them has an icon. This ensures the best appearance for the set of quick actions.

## Parameters

- `contact`: The   contact object to derive the icon from.

## See Also

- [convenience init(type: UIApplicationShortcutIcon.IconType)](uiapplicationshortcuticon/init(type:).md)
  Creates a Home Screen quick action icon using a system-defined image.
- [convenience init(templateImageName: String)](uiapplicationshortcuticon/init(templateimagename:).md)
  Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [convenience init(systemImageName: String)](uiapplicationshortcuticon/init(systemimagename:).md)
  Creates a Home Screen quick action icon using a system symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(contact:))*