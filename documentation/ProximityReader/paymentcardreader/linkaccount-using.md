# linkAccount(using:)

**Framework**: Proximityreader  
**Kind**: method

Presents a sheet for the merchant to accept Tap to Pay on iPhone’s Terms and Conditions on a device.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
func linkAccount(using token: PaymentCardReader.Token) async throws
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Discussion

To use Tap to Pay on iPhone, your participating payment service provider must provide the merchant using your app with a secure token. This token contains an unique identifier for each merchant. This merchant must accept Tap to Pay on iPhone’s Terms and Conditions. After a merchant accepts the Terms and Conditions for their specific merchant identifier on one device, they don’t need to accept it again on additional devices that use the same identifier.

Use the [`isAccountLinked(using:)`](paymentcardreader/isaccountlinked(using:).md) method to confirm calling [`linkAccount(using:)`](paymentcardreader/linkaccount(using:).md) is required.

If the merchant hasn’t accepted the Terms and Conditions, calling [`prepare(using:)`](paymentcardreader/prepare(using:).md) throws [`PaymentCardReaderError.accountNotLinked`](paymentcardreadererror/accountnotlinked.md).

If the merchant has already accepted the Terms and Conditions, calling this method throws [`PaymentCardReaderError.accountAlreadyLinked`](paymentcardreadererror/accountalreadylinked.md).

> **Note**: [`PaymentCardReaderError.accountAlreadyLinked`](paymentcardreadererror/accountalreadylinked.md) if the merchant already accepted the Tap to Pay on iPhone’s Terms and Conditions. The method throws [`PaymentCardReaderError.accountLinkingFailed`](paymentcardreadererror/accountlinkingfailed.md), [`PaymentCardReaderError.accountLinkingCancelled`](paymentcardreadererror/accountlinkingcancelled.md), or other relevant errors in [`PaymentCardReaderError`](paymentcardreadererror.md) if a problem occurs.

## Parameters

- `token`: The token from your payment service provider. This token contains the   merchant identifier.

## See Also

- [func isAccountLinked(using: PaymentCardReader.Token) async throws -> Bool](paymentcardreader/isaccountlinked(using:).md)
  A Boolean value that indicates whether the account is already linked.
- [func relinkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/relinkaccount(using:).md)
  Presents a sheet for the merchant to re-accept Tap to Pay on iPhone’s Terms and Conditions on a device using a different Apple Account.
- [PaymentCardReader.Token](paymentcardreader/token.md)
  A secure token that you receive from your participating payment service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/linkaccount(using:))*