# PKContactField

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

The fields that describe a contact.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PKContactField
```

#### Discussion

Use [`PKContactField`](pkcontactfield.md) field types to indicate which contact fields you require for a billing or shipping contact in order to complete the transaction.

## Topics

### Initializing a contact field
- [init(rawValue: String)](pkcontactfield/init(rawvalue:).md)
  Create a contact field given the raw value.
### Types of contact fields
- [static let emailAddress: PKContactField](pkcontactfield/emailaddress.md)
  A constant that indicates a contact’s email address.
- [static let name: PKContactField](pkcontactfield/name.md)
  A constant that indicates a contact’s name.
- [static let phoneNumber: PKContactField](pkcontactfield/phonenumber.md)
  A constant that indicates a contact’s telephone number.
- [static let phoneticName: PKContactField](pkcontactfield/phoneticname.md)
  A constant that indicates a contact’s phonetic name.
- [static let postalAddress: PKContactField](pkcontactfield/postaladdress.md)
  A constant that indicates a contact’s postal address.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var requiredBillingContactFields: Set<PKContactField>](pkpaymentrequest/requiredbillingcontactfields.md)
  A list of fields that you need for a billing contact to process the transaction.
- [var requiredShippingContactFields: Set<PKContactField>](pkpaymentrequest/requiredshippingcontactfields.md)
  A list of fields that you need for a shipping contact to process the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkcontactfield)*