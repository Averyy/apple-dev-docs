# MobileDriversLicenseDisplayRequest.Options

**Framework**: ProximityReader  
**Kind**: struct

An object that customizes how to perform a display request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Options
```

#### Overview

Use this object to configure the validation mode of the request.

## Topics

### Structures
- [MobileDriversLicenseDisplayRequest.Options.ValidationMode](mobiledriverslicensedisplayrequest/options-swift.struct/validationmode-swift.struct.md)
  A type that represents the validation mode of the mobile document request.
### Operators
- [static func == (MobileDriversLicenseDisplayRequest.Options, MobileDriversLicenseDisplayRequest.Options) -> Bool](mobiledriverslicensedisplayrequest/options-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(validationMode: MobileDriversLicenseDisplayRequest.Options.ValidationMode)](mobiledriverslicensedisplayrequest/options-swift.struct/init(validationmode:).md)
  Creates a mobile document reader display request options type.
### Instance Properties
- [var hashValue: Int](mobiledriverslicensedisplayrequest/options-swift.struct/hashvalue.md)
  The hash value.
- [var validationMode: MobileDriversLicenseDisplayRequest.Options.ValidationMode](mobiledriverslicensedisplayrequest/options-swift.struct/validationmode-swift.property.md)
  The validation mode of the mobile document request.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledriverslicensedisplayrequest/options-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledriverslicensedisplayrequest/options-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var options: MobileDriversLicenseDisplayRequest.Options](mobiledriverslicensedisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest/options-swift.struct)*