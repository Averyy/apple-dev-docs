# addPaymentPassViewController(_:didFinishAdding:error:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, didFinishAdding pass: PKPaymentPass?, error: (any Error)?)
```

#### Discussion

This method is called when the request successfully adds the card to Apple Pay or when the request fails.

## Parameters

- `controller`: The controller adding the pass.
- `pass`: The completed pass, or   if there was an error.
- `error`: If the request failed, this parameter contains an error object using the   error domain. For a list of possible error codes, see the   enum.

## See Also

- [func addPaymentPassViewController(PKAddPaymentPassViewController, generateRequestWithCertificateChain: [Data], nonce: Data, nonceSignature: Data, completionHandler: (PKAddPaymentPassRequest) -> Void)](pkaddpaymentpassviewcontrollerdelegate/addpaymentpassviewcontroller(_:generaterequestwithcertificatechain:nonce:noncesignature:completionhandler:).md)
  Asks the delegate to create an add payment request.
- [class PKAddPaymentPassRequest](pkaddpaymentpassrequest.md)
  Contains the card data needed to add a card to Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate/addpaymentpassviewcontroller(_:didfinishadding:error:))*