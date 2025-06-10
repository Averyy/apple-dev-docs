# MobileNationalIDCardDisplayRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful mobile national ID card display request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Response
```

#### Overview

Use this object to check the validation outcome of the display request.

## Topics

### Operators
- [static func == (MobileNationalIDCardDisplayRequest.Response, MobileNationalIDCardDisplayRequest.Response) -> Bool](mobilenationalidcarddisplayrequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobilenationalidcarddisplayrequest/response/hashvalue.md)
  The hash value.
- [let validationOutcome: MobileNationalIDCardDisplayRequest.Response.ValidationOutcome](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.property.md)
  The value that indicates how the user validated the mobile document response.
### Instance Methods
- [func hash(into: inout Hasher)](mobilenationalidcarddisplayrequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [MobileNationalIDCardDisplayRequest.Response.ValidationOutcome](mobilenationalidcarddisplayrequest/response/validationoutcome-swift.enum.md)
  A type that represents how the user validates the mobile document response.
### Default Implementations
- [Equatable Implementations](mobilenationalidcarddisplayrequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest/response)*