# MobileDocumentReaderSession

**Framework**: ProximityReader  
**Kind**: class

The object you use to start reading a mobile document.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
final class MobileDocumentReaderSession
```

## Mentions

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)
- [Generating reader tokens for the Verifier API](generating-reader-tokens-for-the-verifier-api.md)

#### Overview

Use a `MobileDocumentReaderSession` object to read mobile documents from a properly configured device. Don’t create this object directly. Instead, obtain one by calling the [`prepare(using:)`](mobiledocumentreader/prepare(using:).md) method of your [`MobileDocumentReader`](mobiledocumentreader.md) object. This returns a session after the successful configuration of the device.

Maintain a strong reference to a session object for the duration of the document-reading process. You may use the same session object to perform multiple read operations, but you may perform only one read operation at a time from the device.

## Topics

### Performing a document request
- [func requestDocument<Request>(Request) async throws -> Request.Response](mobiledocumentreadersession/requestdocument(_:).md)
  Presents a sheet to read a mobile document and returns the relevant response.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)
  Configure and test ID Verifier support in your app for reading mobile documents.
- [Generating reader tokens for the Verifier API](generating-reader-tokens-for-the-verifier-api.md)
  Configure your server to generate reader tokens to prepare a device for mobile document reading.
- [Checking IDs with the Verifier API](checking-ids-with-the-verifier-api.md)
  Read and verify mobile driver’s license information without any additional hardware.
- [class MobileDocumentReader](mobiledocumentreader.md)
  An object for configuring mobile document reading on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadersession)*