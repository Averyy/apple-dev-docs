# language

**Framework**: MapKit JS  
**Kind**: property

A language ID indicating the selected language.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get language(): string;
set language(language: string);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

The ID of the language you pass as an initialization option, or according to the user’s browser preference. You can change the language property dynamically, which no longer requires that you reload the containing page. If the language choice isn’t available, MapKit JS picks the best match.

For more information about language IDs, see [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html).

## See Also

- [build](mapkit/build.md)
  The build string.
- [version](mapkit/version.md)
  The version of MapKit JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit/language)*