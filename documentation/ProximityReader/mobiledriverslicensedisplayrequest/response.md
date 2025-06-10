# MobileDriversLicenseDisplayRequest.Response

**Framework**: ProximityReader  
**Kind**: struct

A type that contains the response information from a successful mobile driver’s license display request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Response
```

#### Overview

Use this object to check the validation outcome of the display request.

## Topics

### Operators
- [static func == (MobileDriversLicenseDisplayRequest.Response, MobileDriversLicenseDisplayRequest.Response) -> Bool](mobiledriverslicensedisplayrequest/response/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledriverslicensedisplayrequest/response/hashvalue.md)
  The hash value.
- [let validationOutcome: MobileDriversLicenseDisplayRequest.Response.ValidationOutcome](mobiledriverslicensedisplayrequest/response/validationoutcome-swift.property.md)
  The value that indicates how the user validated the mobile document response.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicensedisplayrequest/response/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [MobileDriversLicenseDisplayRequest.Response.ValidationOutcome](mobiledriverslicensedisplayrequest/response/validationoutcome-swift.enum.md)
  A type that represents how the user validates the mobile document response.
### Default Implementations
- [Equatable Implementations](mobiledriverslicensedisplayrequest/response/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest/response)*