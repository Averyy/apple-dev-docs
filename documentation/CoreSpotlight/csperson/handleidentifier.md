# handleIdentifier

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSString * handleIdentifier;
```

## Discussion

The value of this property is a [`CNContact`](../../Contacts/cncontact.md) property key, such as [`CNContactPhoneNumbersKey`](../../Contacts/cncontactphonenumberskey.md) or [`CNContactEmailAddressesKey`](../../Contacts/cncontactemailaddresseskey.md).

## See Also

### Accessing person properties
- [var contactIdentifier: String?](./contactidentifier.md)
  The identifier for the contact associated with the person.
- [var displayName: String?](./displayname.md)
  A display name for the person.
- [var handles: [String]](./handles.md)
  An array of contact handles related to the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson/handleidentifier)*