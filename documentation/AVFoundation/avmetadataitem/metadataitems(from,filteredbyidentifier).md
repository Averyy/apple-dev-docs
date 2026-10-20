# metadataItems(from:filteredByIdentifier:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns metadata items for the specified identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], filteredByIdentifier identifier: AVMetadataIdentifier) -> [AVMetadataItem]
```

```objc
+ (NSArray<AVMetadataItem *> *) metadataItemsFromArray:(NSArray<AVMetadataItem *> *) metadataItems filteredByIdentifier:(AVMetadataIdentifier) identifier;
```

## Mentions

- [Retrieving media metadata](../retrieving-media-metadata.md)

#### Return Value

An array of metadata items that match the specified identifier.

## Parameters

- `metadataItems`: The metadata items to filter.
- `identifier`: The identifier of the metadata items to retrieve.

## See Also

### Filtering arrays of metadata items
- [class func metadataItems(from: [AVMetadataItem], withKey: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]](./metadataitems%28from,withkey,keyspace%29.md)
  Returns metadata items that match a specified key or key space.
- [class func metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem]](./metadataitems%28from,with%29.md)
  Returns metadata items that match a specified locale.
- [class func metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem]](./metadataitems%28from,filteredandsortedaccordingtopreferredlanguages%29.md)
  Returns metadata items whose locales match one of the specified language identifiers.
- [class func metadataItems(from: [AVMetadataItem], filteredBy: AVMetadataItemFilter) -> [AVMetadataItem]](./metadataitems%28from,filteredby%29.md)
  Returns filtered metadata items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredbyidentifier:))*