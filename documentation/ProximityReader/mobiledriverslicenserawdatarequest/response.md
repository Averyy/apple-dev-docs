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

### Operators
- [static func == (MobileDriversLicenseRawDataRequest.Response, MobileDriversLicenseRawDataRequest.Response) -> Bool](mobiledriverslicenserawdatarequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledriverslicenserawdatarequest/response/hashvalue.md)
  The hash value.
- [let responseData: Data](mobiledriverslicenserawdatarequest/response/responsedata.md)
  The data the mobile driver’s license holder returns.
- [let sessionTranscript: Data](mobiledriverslicenserawdatarequest/response/sessiontranscript.md)
  The session transcript of the document request.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicenserawdatarequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledriverslicenserawdatarequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest/response)*