# PKPaymentInformationRequestHandling

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol PKPaymentInformationRequestHandling
```

#### Overview

> ❗ **Important**:  Before you can add a QR code purchase extension you need an entitlement from Apple. For more information on requesting an entitlement, contact apple-pay-inquiries@apple.com.

 Before you can add a QR code purchase extension you need an entitlement from Apple. For more information on requesting an entitlement, contact apple-pay-inquiries@apple.com.

## Topics

### Getting the transaction information
- [func handle(PKBarcodeEventConfigurationRequest, completion: () -> Void)](pkpaymentinformationrequesthandling/handle(_:completion:)-3cth8.md)
- [func handleInformationRequest(PKBarcodeEventMetadataRequest, completion: PKInformationRequestCompletionBlock)](pkpaymentinformationrequesthandling/handleinformationrequest(_:completion:).md)
- [class PKBarcodeEventConfigurationRequest](pkbarcodeeventconfigurationrequest.md)
- [class PKBarcodeEventMetadataRequest](pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](pkbarcodeeventmetadataresponse.md)
- [typealias PKInformationRequestCompletionBlock](pkinformationrequestcompletionblock.md)
### Signing the transaction
- [func handle(PKBarcodeEventSignatureRequest, completion: PKSignatureRequestCompletionBlock)](pkpaymentinformationrequesthandling/handle(_:completion:)-18x2y.md)
- [class PKBarcodeEventSignatureRequest](pkbarcodeeventsignaturerequest.md)
- [class PKBarcodeEventSignatureResponse](pkbarcodeeventsignatureresponse.md)
- [typealias PKSignatureRequestCompletionBlock](pksignaturerequestcompletionblock.md)

## See Also

- [class PKPaymentInformationEventExtension](pkpaymentinformationeventextension.md)
  An abstract superclass for an extension to collect payment information and sign transaction data in a QR code purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentinformationrequesthandling)*