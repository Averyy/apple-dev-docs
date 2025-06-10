# MobileDocumentAnyOfRawDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful raw data request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Response
```

## Topics

### Operators
- [static func == (MobileDocumentAnyOfRawDataRequest.Response, MobileDocumentAnyOfRawDataRequest.Response) -> Bool](mobiledocumentanyofrawdatarequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledocumentanyofrawdatarequest/response/hashvalue.md)
  The hash value.
- [let responseData: Data](mobiledocumentanyofrawdatarequest/response/responsedata.md)
  The data the document holder returns.
- [let sessionTranscript: Data](mobiledocumentanyofrawdatarequest/response/sessiontranscript.md)
  The session transcript of the document request.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentanyofrawdatarequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentanyofrawdatarequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofrawdatarequest/response)*