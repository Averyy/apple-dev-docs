# DataDetector.Match.SemanticDetails.PostalAddress

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

A match that the data detector determines represents a postal address.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct PostalAddress
```

## Discussion

The data detector attempts to populate as much of the postal address as possible. The properties the detector supports include:

- [`fullAddress`](./postaladdress/fulladdress.md) contains the full string of the address and may contain more than just the sum of the individual components.
- [`street`](./postaladdress/street.md) may contain the street component of the address.
- [`city`](./postaladdress/city.md) may contain the city component of the address.
- [`state`](./postaladdress/state.md) may contain the state component of the address.
- [`postalCode`](./postaladdress/postalcode.md) may contain the postal code component of the address.
- [`region`](./postaladdress/region.md) may contain the region component of the address, for example, United States or France.
- [`regionCode`](./postaladdress/regioncode.md) may contain the ISO region code of the address.
- [`label`](./postaladdress/label.md) may contain a value suitable to populate a label when creating a contact.

## Topics

### Properties that detail parts of a postal address
- [let fullAddress: String](./postaladdress/fulladdress.md)
  A string that contains the full string of the address.
- [let street: String?](./postaladdress/street.md)
  An optional string that may contain the street component of the address.
- [let city: String?](./postaladdress/city.md)
  An optional string that may contain the city component of the address.
- [let state: String?](./postaladdress/state.md)
  An optional string that may contain the state component of the address.
- [let postalCode: String?](./postaladdress/postalcode.md)
  An optional string that may contain the postal code component of the address.
- [let region: String?](./postaladdress/region.md)
  An optional string that may contain the region component of the address.
- [let regionCode: Locale.Region?](./postaladdress/regioncode.md)
  An optional string that may contain the standard ISO 3166 region code of the address.
- [let label: String?](./postaladdress/label.md)
  An optional string that may contain a value suitable to populate a label when creating a contact.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/postaladdress)*