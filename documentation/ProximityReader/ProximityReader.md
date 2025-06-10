# ProximityReader

**Framework**: ProximityReader  
**Kind**: module

Read contactless physical and digital wallet cards using your iPhone.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Mentions

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)
- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Overview

The ProximityReader framework supports , which allows a person’s iPhone to act as a point-of-sale device without additional hardware. ProximityReader also supports the reading of loyalty cards from the Wallet app. Use this framework to initiate the payment process from your app.

The use of this framework requires you to coordinate with a participating payment service provider that is Level 3 certified. Contact your payment provider and work with them to set up a workflow for handling payments. When you’re ready, contact Apple and request the entitlement you need to integrate Tap to Pay on iPhone support into your app. For information on requesting this entitlement, see [`Setting up Tap to Pay on iPhone`](setting-up-the-entitlement-for-tap-to-pay-on-iphone.md).

> **Note**: Tap to Pay on iPhone follows the PCI CPoC Standard, which uses Level 2 certified payment kernels and a user interface for reading contactless payment cards.

## Topics

### Payment card reader
- [Setting up Tap to Pay on iPhone](setting-up-the-entitlement-for-tap-to-pay-on-iphone.md)
  Request and configure the required entitlement to support Tap to Pay on iPhone.
- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)
  Configure your app to use Tap to Pay on iPhone to read contactless payment cards.
- [class PaymentCardReader](paymentcardreader.md)
  An object you use to configure Tap to Pay on iPhone on the current device.
- [class PaymentCardReaderSession](paymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card.
### Payment requests
- [struct PaymentCardTransactionRequest](paymentcardtransactionrequest.md)
  A request for a contactless purchase or refund that includes the purchase amount and currency information.
- [struct PaymentCardVerificationRequest](paymentcardverificationrequest.md)
  A request to verify details for a contactless payment card.
- [struct PaymentCardReadResult](paymentcardreadresult.md)
  The result of a payment card read operation.
### Store and Forward mode
- [struct StoreAndForwardBatch](storeandforwardbatch.md)
  A structure that stores the data to send to the payment service provider to process.
- [struct StoreAndForwardBatchDeletionToken](storeandforwardbatchdeletiontoken.md)
  A secure token that you use to delete a Store and Forward batch.
- [class StoreAndForwardPaymentCardReaderSession](storeandforwardpaymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- [struct StoreAndForwardStatus](storeandforwardstatus.md)
  A structure that describes the Store and Forward session status.
- [struct PaymentCardReaderStore](paymentcardreaderstore.md)
  A structure that manages the store that contains all the Store and Forward reads.
### Loyalty card requests
- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)
  Set up the necessary components so your app can begin using Tap to Pay on iPhone to read and issue loyalty passes.
- [class VASRequest](vasrequest.md)
  A request to read a contactless loyalty card and retrieve loyalty program identifiers for the person.
- [struct VASReadResult](vasreadresult.md)
  The result of a request to read loyalty card information.
### Merchant discovery
- [class ProximityReaderDiscovery](proximityreaderdiscovery.md)
  An object that presents a UI with information about how to use Tap to Pay on iPhone.
### Mobile document reader
- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)
  Configure and test ID Verifier support in your app for reading mobile documents.
- [Generating reader tokens for the Verifier API](generating-reader-tokens-for-the-verifier-api.md)
  Configure your server to generate reader tokens to prepare a device for mobile document reading.
- [Checking IDs with the Verifier API](checking-ids-with-the-verifier-api.md)
  Read and verify mobile driver’s license information without any additional hardware.
- [class MobileDocumentReader](mobiledocumentreader.md)
  An object for configuring mobile document reading on the current device.
- [class MobileDocumentReaderSession](mobiledocumentreadersession.md)
  The object you use to start reading a mobile document.
### Mobile document requests
- [struct MobileDriversLicenseDisplayRequest](mobiledriverslicensedisplayrequest.md)
  A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileDriversLicenseDataRequest](mobiledriverslicensedatarequest.md)
  A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileDriversLicenseRawDataRequest](mobiledriverslicenserawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileNationalIDCardDisplayRequest](mobilenationalidcarddisplayrequest.md)
  A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [struct MobileNationalIDCardDataRequest](mobilenationalidcarddatarequest.md)
  A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [struct MobileNationalIDCardRawDataRequest](mobilenationalidcardrawdatarequest.md)
  A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentDisplayRequest](mobiledocumentdisplayrequest.md)
  A mobile document request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [protocol MobileDocumentRequest](mobiledocumentrequest.md)
  A type that represents a mobile document request.
- [protocol MobileDocumentDataRequest](mobiledocumentdatarequest.md)
  A type that represents a mobile document data request.
- [protocol MobileDocumentRawDataRequest](mobiledocumentrawdatarequest.md)
  A type that represents a mobile document raw data request.
- [struct MobilePhotoIDDataRequest](mobilephotoiddatarequest.md)
  A photo ID request that retrieves elements from the holder and returns the validated document elements.
- [struct MobilePhotoIDRawDataRequest](mobilephotoidrawdatarequest.md)
  A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [struct MobileDocumentAnyOfDataRequest](mobiledocumentanyofdatarequest.md)
  A type that describes a data request for any mobile document from a group of requests.
- [struct MobileDocumentAnyOfRawDataRequest](mobiledocumentanyofrawdatarequest.md)
  A type that describes a raw data request for any mobile document from a group of requests.
### Errors
- [enum PaymentCardReaderError](paymentcardreadererror.md)
  An error type that indicates problems with the configuration of the reader.
- [enum MobileDocumentReaderError](mobiledocumentreadererror.md)
  An error type that indicates problems when preparing a mobile document reader session and performing document requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ProximityReader)*