# language

**Framework**: MapKit JS  
**Kind**: property

A language ID that determines the language for the search results text.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
language?: string;
```

#### Discussion

If you set a language ID, the search returns addresses in the selected language, if available, such as, `fr-CA` or `en-GB`. If you don’t provide a language ID, the search object uses the language ID the system provides to the [`init(options)`](mapkit/init.md) call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions/language)*