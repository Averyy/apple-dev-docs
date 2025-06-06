# init(forNewContact:)

**Framework**: Contacts UI  
**Kind**: init

Initializes a view controller for a new contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(forNewContact contact: CNContact?)
```

#### Return Value

A newly initialized [`CNContactViewController`](cncontactviewcontroller.md) object.

#### Discussion

This view controller initializes the customized behavior and appearance of [`CNContactViewController`](cncontactviewcontroller.md) for a new contact.

## Parameters

- `contact`: The contact to be displayed.

## See Also

- [convenience init(for: CNContact)](cncontactviewcontroller/init(for:).md)
  Initializes a view controller for an existing contact.
- [convenience init(forContact: CNContact)](cncontactviewcontroller/init(forcontact:).md)
  Initializes a view controller for an existing contact.
- [convenience init(forUnknownContact: CNContact)](cncontactviewcontroller/init(forunknowncontact:).md)
  Initializes a view controller for an unknown contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/init(fornewcontact:))*