# MobileDriversLicenseRawDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful mobile driver’s license raw data request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Response
```

## Topics

### Instance Properties
- [let ephemeralReaderKey: Data](mobiledriverslicenserawdatarequest/response/ephemeralreaderkey.md)
  The session’s ephemeral reader key.
- [let responseData: Data](mobiledriverslicenserawdatarequest/response/responsedata.md)
  The data the mobile driver’s license holder returns.
- [let sessionTranscript: Data](mobiledriverslicenserawdatarequest/response/sessiontranscript.md)
  The session transcript of the document request.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest/response)*