# relinkAccount(using:)

**Framework**: ProximityReader  
**Kind**: method

Presents a sheet for the merchant to re-accept Tap to Pay on iPhone’s Terms and Conditions on a device using a different Apple Account.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 17.0+

## Declaration

```swift
func relinkAccount(using token: PaymentCardReader.Token) async throws
```

#### Discussion

To use Tap to Pay on iPhone, your participating payment service provider must provide the merchant using your app with a secure token. This token contains a unique identifier for each merchant and also specifies if relinking using a different Apple Account is allowed.

To use this method, a merchant must have already accepted the Terms and Conditions using [`linkAccount(using:)`](paymentcardreader/linkaccount(using:).md).

After a merchant accepts the Terms and Conditions for their specific merchant identifier on one device, they don’t need to accept it again on additional devices that use the same identifier.

> **Note**: [`PaymentCardReaderError.accountLinkingFailed`](paymentcardreadererror/accountlinkingfailed.md), [`PaymentCardReaderError.accountLinkingCancelled`](paymentcardreadererror/accountlinkingcancelled.md), or other relevant errors in [`PaymentCardReaderError`](paymentcardreadererror.md).

## Parameters

- `token`: The token from your payment service provider. This token contains the merchant identifier and must include permission for relinking.

## See Also

- [func isAccountLinked(using: PaymentCardReader.Token) async throws -> Bool](paymentcardreader/isaccountlinked(using:).md)
  A Boolean value that indicates whether the account is already linked.
- [func linkAccount(using: PaymentCardReader.Token) async throws](paymentcardreader/linkaccount(using:).md)
  Presents a sheet for the merchant to accept Tap to Pay on iPhone’s Terms and Conditions on a device.
- [PaymentCardReader.Token](paymentcardreader/token.md)
  A secure token that you receive from your participating payment service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/relinkaccount(using:))*