# metadataItems(from:with:)

**Framework**: AVFoundation  
**Kind**: method

Returns metadata items that match a specified locale.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], with locale: Locale) -> [AVMetadataItem]
```

#### Return Value

An array of metadata items that match the specified key and key space.

## Parameters

- `metadataItems`: The metadata items to filter.
- `locale`: The locale of the metadata items to retrieve.

## See Also

- [class func metadataItems(from: [AVMetadataItem], filteredByIdentifier: AVMetadataIdentifier) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredbyidentifier:).md)
  Returns metadata items for the specified identifier.
- [class func metadataItems(from: [AVMetadataItem], withKey: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:withkey:keyspace:).md)
  Returns metadata items that match a specified key or key space.
- [class func metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns metadata items whose locales match one of the specified language identifiers.
- [class func metadataItems(from: [AVMetadataItem], filteredBy: AVMetadataItemFilter) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredby:).md)
  Returns filtered metadata items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:with:))*