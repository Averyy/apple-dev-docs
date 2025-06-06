# isAccountLinked(using:)

**Framework**: Proximityreader  
**Kind**: method

A Boolean value that indicates whether the account is already linked.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
func isAccountLinked(using token: PaymentCardReader.Token) async throws -> Bool
```

#### Discussion

Call [`linkAccount(using:)`](paymentcardreader/linkaccount(using:).md) to link an account.

> **Note**: If [`prepare(using:)`](paymentcardreader/prepare(using:).md) throws an [`PaymentCardReaderError.accountNotLinked`](paymentcardreadererror/accountnotlinked.md) error call [`linkAccount(using:)`](paymentcardreader/linkaccount(using:).md) again to relink the account.

> **Note**: [`PaymentCardReaderError`](paymentcardreadererror.md)

## Parameters

- `token`: The token from your payment service provider. This token contains the merchant identifier.

## See Also

- [func linkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/linkaccount(using:).md)
  Presents a sheet for the merchant to accept Tap to Pay on iPhone’s Terms and Conditions on a device.
- [func relinkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/relinkaccount(using:).md)
  Presents a sheet for the merchant to re-accept Tap to Pay on iPhone’s Terms and Conditions on a device using a different Apple Account.
- [PaymentCardReader.Token](paymentcardreader/token.md)
  A secure token that you receive from your participating payment service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/isaccountlinked(using:))*