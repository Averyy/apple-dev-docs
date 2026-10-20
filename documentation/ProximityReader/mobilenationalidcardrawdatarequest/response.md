# MobileNationalIDCardRawDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

A type that contains the response information from a successful mobile national ID card raw data request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
struct Response
```

## Topics

### Instance Properties
- [let ephemeralReaderKey: Data](./response/ephemeralreaderkey.md)
  The session’s ephemeral reader key.
- [let responseData: Data](./response/responsedata.md)
  The data the mobile national ID card holder returns.
- [let sessionTranscript: Data](./response/sessiontranscript.md)
  The session transcript of the document request.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest/response)*