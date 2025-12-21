# language

**Framework**: MapKit JS  
**Kind**: property

A language ID that determines the language for route information.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
language?: string;
```

#### Discussion

When you set the language to a language ID such as `fr-CA` or `en-GB`, MapKit JS returns step-by-step directions in the specified language, if available. If you don’t set the language when initializing a [`Directions`](directions.md) object, the directions default to the language ID the system provides when initializing the map with [`init(options)`](mapkit/init.md). If the map doesn’t have a specified language upon initialization, MapKit JS returns directions in the browser’s language setting.

For more information about language IDs, see [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/directionsconstructoroptions/language)*