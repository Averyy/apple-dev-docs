# MobileDocumentAnyOfDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful data request.

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
- [static func == (MobileDocumentAnyOfDataRequest.Response, MobileDocumentAnyOfDataRequest.Response) -> Bool](mobiledocumentanyofdatarequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var documentResponse: any MobileDocumentDataResponse](mobiledocumentanyofdatarequest/response/documentresponse.md)
  The document response from a successful request.
- [var hashValue: Int](mobiledocumentanyofdatarequest/response/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentanyofdatarequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentanyofdatarequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofdatarequest/response)*