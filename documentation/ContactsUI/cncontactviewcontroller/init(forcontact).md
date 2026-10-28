# init(forContact:)

**Framework**: Contacts UI  
**Kind**: init  
**Role**: Initializer

Initializes a view controller for an existing contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(forContact contact: CNContact)
```

## Return Value

A newly initialized [`CNContactViewController`](../cncontactviewcontroller.md) object.

## Discussion

This view controller initializes the customized behavior and appearance of [`CNContactViewController`](../cncontactviewcontroller.md) for a contact.

## Parameters

- `contact`: The existing contact.

## See Also

### Creating the Contact Viewer
- [convenience init(for: CNContact)](./init%28for%29.md)
  Initializes a view controller for an existing contact.
- [convenience init(forUnknownContact: CNContact)](./init%28forunknowncontact%29.md)
  Initializes a view controller for an unknown contact.
- [convenience init(forNewContact: CNContact?)](./init%28fornewcontact%29.md)
  Initializes a view controller for a new contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/init(forcontact:))*