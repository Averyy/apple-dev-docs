# MobilePhotoIDRawDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful photo ID raw data request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Response
```

## Topics

### Instance Properties
- [let ephemeralReaderKey: Data](mobilephotoidrawdatarequest/response/ephemeralreaderkey.md)
  The session’s ephemeral reader key.
- [let responseData: Data](mobilephotoidrawdatarequest/response/responsedata.md)
  The data the photo ID holder returns.
- [let sessionTranscript: Data](mobilephotoidrawdatarequest/response/sessiontranscript.md)
  The session transcript of the document request.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest/response)*