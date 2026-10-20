# MobileDriversLicenseRawDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

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
- [let ephemeralReaderKey: Data](./response/ephemeralreaderkey.md)
  The session’s ephemeral reader key.
- [let responseData: Data](./response/responsedata.md)
  The data the mobile driver’s license holder returns.
- [let sessionTranscript: Data](./response/sessiontranscript.md)
  The session transcript of the document request.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest/response)*