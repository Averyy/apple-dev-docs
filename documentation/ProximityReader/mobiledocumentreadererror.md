# MobileDocumentReaderError

**Framework**: ProximityReader  
**Kind**: enum

An error type that indicates problems when preparing a mobile document reader session and performing document requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
enum MobileDocumentReaderError
```

## Mentions

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md)

## Topics

### Getting the error code
- [MobileDocumentReaderError.cancelled](mobiledocumentreadererror/cancelled.md)
  An error that indicates the mobile document request was canceled.
- [MobileDocumentReaderError.invalidRequest](mobiledocumentreadererror/invalidrequest.md)
  An error that indicates the request isn’t valid.
- [MobileDocumentReaderError.invalidResponse](mobiledocumentreadererror/invalidresponse.md)
  An error that indicates the response isn’t valid.
- [MobileDocumentReaderError.invalidToken](mobiledocumentreadererror/invalidtoken.md)
  An error that indicates the provided reader token for framework’s prepare method isn’t valid.
- [MobileDocumentReaderError.networkUnavailable](mobiledocumentreadererror/networkunavailable.md)
  An error that indicates the system can’t reach the network.
- [MobileDocumentReaderError.notAllowed](mobiledocumentreadererror/notallowed.md)
  An error that indicates the device isn’t allowed to perform the mobile document request.
- [MobileDocumentReaderError.notSupported](mobiledocumentreadererror/notsupported.md)
  An error that indicates mobile document reading isn’t supported on the current device.
- [MobileDocumentReaderError.serviceUnavailable](mobiledocumentreadererror/serviceunavailable.md)
  An error that occurs when mobile document reader service is unavailable.
- [MobileDocumentReaderError.sessionExpired](mobiledocumentreadererror/sessionexpired.md)
  An error that indicates the current reader session has expired.
- [MobileDocumentReaderError.systemBusy](mobiledocumentreadererror/systembusy.md)
  An error that indicates the system is busy.
- [MobileDocumentReaderError.unknown](mobiledocumentreadererror/unknown.md)
  An error that indicates the framework encountered a problem which the system can’t interpret.
### Operators
- [static func == (MobileDocumentReaderError, MobileDocumentReaderError) -> Bool](mobiledocumentreadererror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var errorDescription: String?](mobiledocumentreadererror/errordescription.md)
  A localized message describing what error occurred.
- [var hashValue: Int](mobiledocumentreadererror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentreadererror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentreadererror/equatable-implementations.md)
- [Error Implementations](mobiledocumentreadererror/error-implementations.md)
- [LocalizedError Implementations](mobiledocumentreadererror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum PaymentCardReaderError](paymentcardreadererror.md)
  An error type that indicates problems with the configuration of the reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadererror)*