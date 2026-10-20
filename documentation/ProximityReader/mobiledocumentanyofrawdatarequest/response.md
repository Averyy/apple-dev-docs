# MobileDocumentAnyOfRawDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that contains the response information from a successful raw data request.

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
- [let ephemeralReaderKey: Data](./response/ephemeralreaderkey.md)
  The session’s ephemeral reader key.
- [let responseData: Data](./response/responsedata.md)
  The data the document holder returns.
- [let sessionTranscript: Data](./response/sessiontranscript.md)
  The session transcript of the document request.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofrawdatarequest/response)*