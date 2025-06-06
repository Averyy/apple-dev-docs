# commonMetadata

**Framework**: AVFoundation  
**Kind**: property

An array of metadata items for each common metadata key for which a value is available.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var commonMetadata: [AVMetadataItem] { get }
```

#### Discussion

You can filter the array of [`AVMetadataItem`](avmetadataitem.md) objects according to locale using [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md), key using [`metadataItems(from:withKey:keySpace:)`](avmetadataitem/metadataitems(from:withkey:keyspace:).md), or language using [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md).

Clients that are filtering media selection options by language should be prepared to handle cases in which the [`extendedLanguageTag`](avmediaselectionoption/extendedlanguagetag.md) property value is `nil`. Further, they should be prepared to handle cases in which an `extendedLanguageTag` is present but indicates that the language is “undetermined” (a language value of @“und”, as defined in ISO 639-2).

## See Also

- [var availableMetadataFormats: [String]](avmediaselectionoption/availablemetadataformats.md)
  The metadata formats that contain metadata associated with the option.
- [func metadata(forFormat: String) -> [AVMetadataItem]](avmediaselectionoption/metadata(forformat:).md)
  Returns an array of metadata items—one for each metadata item in the container of a given format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/commonmetadata)*