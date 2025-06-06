# metadataItems(from:withKey:keySpace:)

**Framework**: AVFoundation  
**Kind**: method

Returns metadata items that match a specified key or key space.

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
class func metadataItems(from metadataItems: [AVMetadataItem], withKey key: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]
```

#### Return Value

An array of metadata items that match the specified key and key space.

## Parameters

- `metadataItems`: The metadata items to filter.
- `key`: The key of the metadata items to retrieve, or   if you don’t want to filter by key.
- `keySpace`: The key space of the metadata items to retrieve, or   if you don’t want to filter by key space.

## See Also

- [class func metadataItems(from: [AVMetadataItem], filteredByIdentifier: AVMetadataIdentifier) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredbyidentifier:).md)
  Returns metadata items for the specified identifier.
- [class func metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:with:).md)
  Returns metadata items that match a specified locale.
- [class func metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns metadata items whose locales match one of the specified language identifiers.
- [class func metadataItems(from: [AVMetadataItem], filteredBy: AVMetadataItemFilter) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredby:).md)
  Returns filtered metadata items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:withkey:keyspace:))*