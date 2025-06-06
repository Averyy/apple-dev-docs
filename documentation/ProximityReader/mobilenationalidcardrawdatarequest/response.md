# MobileNationalIDCardRawDataRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful mobile national ID card raw data request.

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

### Operators
- [static func == (MobileNationalIDCardRawDataRequest.Response, MobileNationalIDCardRawDataRequest.Response) -> Bool](mobilenationalidcardrawdatarequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobilenationalidcardrawdatarequest/response/hashvalue.md)
  The hash value.
- [let responseData: Data](mobilenationalidcardrawdatarequest/response/responsedata.md)
  The data the mobile national ID card holder returns.
- [let sessionTranscript: Data](mobilenationalidcardrawdatarequest/response/sessiontranscript.md)
  The session transcript of the document request.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcardrawdatarequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobilenationalidcardrawdatarequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest/response)*