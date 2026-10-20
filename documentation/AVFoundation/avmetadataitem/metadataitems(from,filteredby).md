# metadataItems(from:filteredBy:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSArray<AVMetadataItem *> *) metadataItemsFromArray:(NSArray<AVMetadataItem *> *) metadataItems filteredByMetadataItemFilter:(AVMetadataItemFilter *) metadataItemFilter;
```

#### Return Value

The filtered array of metadata items.

## Parameters

- `metadataItems`: The metadata items to filter.
- `metadataItemFilter`: The metadata item filter to apply.

## See Also

### Filtering arrays of metadata items
- [class func metadataItems(from: [AVMetadataItem], filteredByIdentifier: AVMetadataIdentifier) -> [AVMetadataItem]](./metadataitems%28from,filteredbyidentifier%29.md)
  Returns metadata items for the specified identifier.
- [class func metadataItems(from: [AVMetadataItem], withKey: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]](./metadataitems%28from,withkey,keyspace%29.md)
  Returns metadata items that match a specified key or key space.
- [class func metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem]](./metadataitems%28from,with%29.md)
  Returns metadata items that match a specified locale.
- [class func metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem]](./metadataitems%28from,filteredandsortedaccordingtopreferredlanguages%29.md)
  Returns metadata items whose locales match one of the specified language identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredby:))*