# PKContactField

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

The fields that describe a contact.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
struct PKContactField
```

```c
typedef NSString * PKContactField;
```

#### Discussion

Use [`PKContactField`](./pkcontactfield.md) field types to indicate which contact fields you require for a billing or shipping contact in order to complete the transaction.

## Topics

### Initializing a contact field
- [init(rawValue: String)](./pkcontactfield/init%28rawvalue%29.md)
  Create a contact field given the raw value.
### Types of contact fields
- [static let emailAddress: PKContactField](./pkcontactfield/emailaddress.md)
  A constant that indicates a contact’s email address.
- [static let name: PKContactField](./pkcontactfield/name.md)
  A constant that indicates a contact’s name.
- [static let phoneNumber: PKContactField](./pkcontactfield/phonenumber.md)
  A constant that indicates a contact’s telephone number.
- [static let phoneticName: PKContactField](./pkcontactfield/phoneticname.md)
  A constant that indicates a contact’s phonetic name.
- [static let postalAddress: PKContactField](./pkcontactfield/postaladdress.md)
  A constant that indicates a contact’s postal address.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Requesting billing and shipping contact fields
- [var requiredBillingContactFields: Set<PKContactField>](./pkpaymentrequest/requiredbillingcontactfields.md)
  A list of fields that you need for a billing contact to process the transaction.
- [var requiredShippingContactFields: Set<PKContactField>](./pkpaymentrequest/requiredshippingcontactfields.md)
  A list of fields that you need for a shipping contact to process the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkcontactfield)*