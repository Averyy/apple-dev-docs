# PKContact

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that encapsulates contact information needed for billing and shipping.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKContact
```

#### Overview

Instances contain only the information needed for the given transaction. All other properties are set to `nil`.

## Topics

### Contact information
- [var emailAddress: String?](pkcontact/emailaddress.md)
  The contact’s email address, or `nil` if the contact’s email is not needed for the transaction.
- [var name: PersonNameComponents?](pkcontact/name.md)
  The contact’s first and last name, or `nil` if the contact’s name is not needed for the transaction.
- [var phoneNumber: CNPhoneNumber?](pkcontact/phonenumber.md)
  The contact’s telephone number, or `nil` if the contact’s phone number is not needed for the transaction.
- [var postalAddress: CNPostalAddress?](pkcontact/postaladdress.md)
  The contact’s full postal address.
- [var supplementarySubLocality: String?](pkcontact/supplementarysublocality.md)
  The contact’s sublocality, or `nil` if the sublocality is not needed for the transaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var billingContact: PKContact?](pkpayment/billingcontact.md)
  The user-selected billing address for this transaction.
- [var shippingContact: PKContact?](pkpayment/shippingcontact.md)
  The user-selected shipping address for this transaction.
- [var shippingMethod: PKShippingMethod?](pkpayment/shippingmethod.md)
  The user-selected shipping method for this transaction.
- [class PKShippingMethod](pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkcontact)*