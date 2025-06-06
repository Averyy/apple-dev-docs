# metadataItems(from:filteredBy:)

**Framework**: AVFoundation  
**Kind**: method

Returns filtered metadata items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], filteredBy metadataItemFilter: AVMetadataItemFilter) -> [AVMetadataItem]
```

#### Return Value

The filtered array of metadata items.

## Parameters

- `metadataItems`: The metadata items to filter.
- `metadataItemFilter`: The metadata item filter to apply.

## See Also

- [class func metadataItems(from: [AVMetadataItem], filteredByIdentifier: AVMetadataIdentifier) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredbyidentifier:).md)
  Returns metadata items for the specified identifier.
- [class func metadataItems(from: [AVMetadataItem], withKey: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:withkey:keyspace:).md)
  Returns metadata items that match a specified key or key space.
- [class func metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:with:).md)
  Returns metadata items that match a specified locale.
- [class func metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem]](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns metadata items whose locales match one of the specified language identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredby:))*