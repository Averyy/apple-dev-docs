# PaymentCardReader.Token

**Framework**: ProximityReader  
**Kind**: struct

A secure token that you receive from your participating payment service provider.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Token
```

#### Overview

You must create a secure token to use Tap to Pay on iPhone. Your payment service provider supplies the string you use to create this token. Create your token and pass it to the [`prepare(using:)`](paymentcardreader/prepare(using:).md) method to configure the current device to read cards.

## Topics

### Creating a token
- [init(rawValue: String)](paymentcardreader/token/init(rawvalue:).md)
  Creates a token with the string your payment service provider gave you.
### Getting the token value
- [let rawValue: String](paymentcardreader/token/rawvalue-swift.property.md)
  The raw token string from your payment service provider.
### Type Aliases
- [PaymentCardReader.Token.RawValue](paymentcardreader/token/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](paymentcardreader/token/equatable-implementations.md)
- [RawRepresentable Implementations](paymentcardreader/token/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func isAccountLinked(using: PaymentCardReader.Token) async throws -> Bool](paymentcardreader/isaccountlinked(using:).md)
  A Boolean value that indicates whether the account is already linked.
- [func linkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/linkaccount(using:).md)
  Presents a sheet for the merchant to accept Tap to Pay on iPhone’s Terms and Conditions on a device.
- [func relinkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/relinkaccount(using:).md)
  Presents a sheet for the merchant to re-accept Tap to Pay on iPhone’s Terms and Conditions on a device using a different Apple Account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/token)*