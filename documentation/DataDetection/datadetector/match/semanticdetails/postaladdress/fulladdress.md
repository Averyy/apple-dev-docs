# fullAddress

**Framework**: DataDetection  
**Kind**: property  
**Role**: Instance Property

A string that contains the full string of the address.

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
let fullAddress: String
```

## Discussion

This property may contain more than just the sum of the individual components of the rest of the address components.

## See Also

### Properties that detail parts of a postal address
- [let street: String?](./street.md)
  An optional string that may contain the street component of the address.
- [let city: String?](./city.md)
  An optional string that may contain the city component of the address.
- [let state: String?](./state.md)
  An optional string that may contain the state component of the address.
- [let postalCode: String?](./postalcode.md)
  An optional string that may contain the postal code component of the address.
- [let region: String?](./region.md)
  An optional string that may contain the region component of the address.
- [let regionCode: Locale.Region?](./regioncode.md)
  An optional string that may contain the standard ISO 3166 region code of the address.
- [let label: String?](./label.md)
  An optional string that may contain a value suitable to populate a label when creating a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/postaladdress/fulladdress)*