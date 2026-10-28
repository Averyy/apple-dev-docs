# metadataItems(from:withKey:keySpace:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns metadata items that match a specified key or key space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], withKey key: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]
```

```objc
+ (NSArray<AVMetadataItem *> *) metadataItemsFromArray:(NSArray<AVMetadataItem *> *) metadataItems withKey:(id) key keySpace:(AVMetadataKeySpace) keySpace;
```

## Return Value

An array of metadata items that match the specified key and key space.

## Parameters

- `metadataItems`: The metadata items to filter.
- `key`: The key of the metadata items to retrieve, or `nil` if you don’t want to filter by key.
- `keySpace`: The key space of the metadata items to retrieve, or `nil` if you don’t want to filter by key space.

## See Also

### Filtering arrays of metadata items
- [class func metadataItems(from: [AVMetadataItem], filteredByIdentifier: AVMetadataIdentifier) -> [AVMetadataItem]](./metadataitems%28from,filteredbyidentifier%29.md)
  Returns metadata items for the specified identifier.
- [class func metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem]](./metadataitems%28from,with%29.md)
  Returns metadata items that match a specified locale.
- [class func metadataItems(from: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMetadataItem]](./metadataitems%28from,filteredandsortedaccordingtopreferredlanguages%29.md)
  Returns metadata items whose locales match one of the specified language identifiers.
- [class func metadataItems(from: [AVMetadataItem], filteredBy: AVMetadataItemFilter) -> [AVMetadataItem]](./metadataitems%28from,filteredby%29.md)
  Returns filtered metadata items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:withkey:keyspace:))*