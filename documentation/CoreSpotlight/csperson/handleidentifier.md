# handleIdentifier

**Framework**: Core Spotlight  
**Kind**: property

A key that identifies the type of contact property represented by the person object’s handle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var handleIdentifier: String { get }
```

#### Discussion

The value of this property is a [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) property key, such as [`CNContactPhoneNumbersKey`](https://developer.apple.com/documentation/Contacts/CNContactPhoneNumbersKey) or [`CNContactEmailAddressesKey`](https://developer.apple.com/documentation/Contacts/CNContactEmailAddressesKey).

## See Also

- [var contactIdentifier: String?](csperson/contactidentifier.md)
  The identifier for the contact associated with the person.
- [var displayName: String?](csperson/displayname.md)
  A display name for the person.
- [var handles: [String]](csperson/handles.md)
  An array of contact handles related to the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson/handleidentifier)*