# MobileDocumentDisplayRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful mobile document display request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Response
```

#### Overview

Use this object to check the validation outcome of the display request.

## Topics

### Getting the response
- [let validationOutcome: MobileDocumentDisplayRequest.Response.ValidationOutcome](mobiledocumentdisplayrequest/response/validationoutcome-swift.property.md)
  The value that indicates how the user validated the mobile document response.
- [MobileDocumentDisplayRequest.Response.ValidationOutcome](mobiledocumentdisplayrequest/response/validationoutcome-swift.enum.md)
  A type that represents how the user validates the mobile document response.
### Operators
- [static func == (MobileDocumentDisplayRequest.Response, MobileDocumentDisplayRequest.Response) -> Bool](mobiledocumentdisplayrequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledocumentdisplayrequest/response/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentdisplayrequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentdisplayrequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/response)*