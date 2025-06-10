# MobileNationalIDCardDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful mobile national ID card data request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Response
```

## Topics

### Structures
- [MobileNationalIDCardDataRequest.Response.DocumentElements](mobilenationalidcarddatarequest/response/documentelements-swift.struct.md)
  A type that contains the document elements from a successful mobile national ID card data request.
### Operators
- [static func == (MobileNationalIDCardDataRequest.Response, MobileNationalIDCardDataRequest.Response) -> Bool](mobilenationalidcarddatarequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let documentElements: MobileNationalIDCardDataRequest.Response.DocumentElements](mobilenationalidcarddatarequest/response/documentelements-swift.property.md)
  The document elements from a successful mobile national ID card data request.
- [var hashValue: Int](mobilenationalidcarddatarequest/response/hashvalue.md)
  The hash value.
- [let region: Locale.Region](mobilenationalidcarddatarequest/response/region.md)
  The region of the requested document.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcarddatarequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobilenationalidcarddatarequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MobileDocumentDataResponse](mobiledocumentdataresponse.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddatarequest/response)*