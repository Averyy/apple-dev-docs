# language

**Framework**: MapKit JS  
**Kind**: property

The language to use when displaying the reverse lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
language?: string;
```

#### Discussion

[`language`](geocoderlookupoptions/language.md) is the only option that you can set for the reverse geocoder. For example, `{ language: 'fr-CA' }` tells the server to send results localized to Canadian French. If you set it, this option overrides the language you provide in the Geocoder constructor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderreverselookupoptions/language)*