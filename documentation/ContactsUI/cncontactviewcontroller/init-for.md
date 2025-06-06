# init(for:)

**Framework**: Contacts UI  
**Kind**: init

Initializes a view controller for an existing contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(for contact: CNContact)
```

#### Return Value

A newly initialized [`CNContactViewController`](cncontactviewcontroller.md) object.

#### Discussion

This view controller initializes the customized behavior and appearance of [`CNContactViewController`](cncontactviewcontroller.md) for a contact.

## Parameters

- `contact`: The existing contact.

## See Also

- [convenience init(forContact: CNContact)](cncontactviewcontroller/init(forcontact:).md)
  Initializes a view controller for an existing contact.
- [convenience init(forUnknownContact: CNContact)](cncontactviewcontroller/init(forunknowncontact:).md)
  Initializes a view controller for an unknown contact.
- [convenience init(forNewContact: CNContact?)](cncontactviewcontroller/init(fornewcontact:).md)
  Initializes a view controller for a new contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/init(for:))*