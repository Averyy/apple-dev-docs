# Checking IDs with the Verifier API

**Framework**: ProximityReader

Read and verify mobile driver’s license information without any additional hardware.

**Availability**:
- iOS 17.0+
- Xcode 15.0+

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10114: [`What’s new in Wallet and Apple Pay`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10114/).

##### Configure the Sample Code Project

The project contains two targets:

- `VerifierAPISample-DisplayRequest`: This target is configured to perform a [`MobileDriversLicenseDisplayRequest`](mobiledriverslicensedisplayrequest.md).
- `VerifierAPISample-DataRequest`: This target is configured to perform a [`MobileDriversLicenseDataRequest`](mobiledriverslicensedatarequest.md).

## See Also

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)
  Configure and test ID Verifier support in your app for reading mobile documents.
- [Generating reader tokens for the Verifier API](generating-reader-tokens-for-the-verifier-api.md)
  Configure your server to generate reader tokens to prepare a device for mobile document reading.
- [class MobileDocumentReader](mobiledocumentreader.md)
  An object for configuring mobile document reading on the current device.
- [class MobileDocumentReaderSession](mobiledocumentreadersession.md)
  The object you use to start reading a mobile document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/checking-ids-with-the-verifier-api)*