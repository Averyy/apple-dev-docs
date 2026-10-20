# isAccountLinked(using:)

**Framework**: ProximityReader  
**Kind**: method  
**Role**: Instance Method

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

Call [`linkAccount(using:)`](./linkaccount%28using%29.md) to link an account.

> **Note**: If [`prepare(using:)`](./prepare%28using%29.md) throws an [`PaymentCardReaderError.accountNotLinked`](../paymentcardreadererror/accountnotlinked.md) error call [`linkAccount(using:)`](./linkaccount%28using%29.md) again to relink the account.

> **Throws**: [`PaymentCardReaderError`](../paymentcardreadererror.md)

## Parameters

- `token`: The token from your payment service provider. This token contains the merchant identifier.

## See Also

### Displaying the Tap to Pay on iPhone’s terms and conditions
- [func linkAccount(using: PaymentCardReader.Token) async throws](./linkaccount%28using%29.md)
  Presents a sheet for the merchant to accept Tap to Pay on iPhone’s Terms and Conditions on a device.
- [func relinkAccount(using: PaymentCardReader.Token) async throws](./relinkaccount%28using%29.md)
  Presents a sheet for the merchant to re-accept Tap to Pay on iPhone’s Terms and Conditions on a device using a different Apple Account.
- [PaymentCardReader.Token](./token.md)
  A secure token that you receive from your participating payment service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/isaccountlinked(using:))*