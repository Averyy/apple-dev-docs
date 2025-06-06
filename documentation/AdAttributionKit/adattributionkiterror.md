# AdAttributionKitError

**Framework**: AdAttributionKit  
**Kind**: enum

Values that describe ad attribution error conditions.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
enum AdAttributionKitError
```

## Topics

### Operators
- [static func == (AdAttributionKitError, AdAttributionKitError) -> Bool](adattributionkiterror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [AdAttributionKitError.conversionTagNotSupported](adattributionkiterror/conversiontagnotsupported.md)
  The postback update failed due to an unsupported use of conversion tag
- [AdAttributionKitError.impressionExpired](adattributionkiterror/impressionexpired.md)
  The attribution failed because the impression expired.
- [AdAttributionKitError.invalidConversionTag](adattributionkiterror/invalidconversiontag.md)
  The postback update failed due to an invalid conversion tag
- [AdAttributionKitError.invalidImpressionJWSComponents](adattributionkiterror/invalidimpressionjwscomponents.md)
  The attribution failed due to invalid JWS components.
- [AdAttributionKitError.invalidImpressionJWSHeader](adattributionkiterror/invalidimpressionjwsheader.md)
  The attribution failed due to an invalid JWS header.
- [AdAttributionKitError.invalidImpressionJWSPayload](adattributionkiterror/invalidimpressionjwspayload.md)
  The attribution failed due to an invalid JWS payload.
- [AdAttributionKitError.invalidImpressionJWSSignature](adattributionkiterror/invalidimpressionjwssignature.md)
  The attribution failed due to an invalid JWS signature.
- [AdAttributionKitError.missingAttributionView](adattributionkiterror/missingattributionview.md)
  The attribution failed due to a missing attribution view.
- [AdAttributionKitError.unknown](adattributionkiterror/unknown.md)
  The attribution failed due to an unknown, unrecoverable error.
### Instance Properties
- [var description: String](adattributionkiterror/description.md)
  A string that describes the error.
- [var hashValue: Int](adattributionkiterror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](adattributionkiterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](adattributionkiterror/equatable-implementations.md)
- [Error Implementations](adattributionkiterror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/adattributionkiterror)*