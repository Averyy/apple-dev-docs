# MobileDocumentReaderError.systemBusy

**Framework**: ProximityReader  
**Kind**: case  
**Role**: Case

An error that indicates the system is busy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
case systemBusy
```

#### Discussion

Try to perform the document request again later.

## See Also

### Getting the error code
- [MobileDocumentReaderError.cancelled](./cancelled.md)
  An error that indicates the mobile document request was canceled.
- [MobileDocumentReaderError.invalidRequest](./invalidrequest.md)
  An error that indicates the request isn’t valid.
- [MobileDocumentReaderError.invalidResponse](./invalidresponse.md)
  An error that indicates the response isn’t valid.
- [MobileDocumentReaderError.invalidToken](./invalidtoken.md)
  An error that indicates the provided reader token for framework’s prepare method isn’t valid.
- [MobileDocumentReaderError.networkUnavailable](./networkunavailable.md)
  An error that indicates the system can’t reach the network.
- [MobileDocumentReaderError.notAllowed](./notallowed.md)
  An error that indicates the device isn’t allowed to perform the mobile document request.
- [MobileDocumentReaderError.notSupported](./notsupported.md)
  An error that indicates mobile document reading isn’t supported on the current device.
- [MobileDocumentReaderError.serviceUnavailable](./serviceunavailable.md)
  An error that occurs when mobile document reader service is unavailable.
- [MobileDocumentReaderError.sessionExpired](./sessionexpired.md)
  An error that indicates the current reader session has expired.
- [MobileDocumentReaderError.unknown](./unknown.md)
  An error that indicates the framework encountered a problem which the system can’t interpret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadererror/systembusy)*