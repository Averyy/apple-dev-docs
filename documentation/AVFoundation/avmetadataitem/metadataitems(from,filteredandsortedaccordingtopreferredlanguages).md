# metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns metadata items whose locales match one of the specified language identifiers.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func metadataItems(from metadataItems: [AVMetadataItem], filteredAndSortedAccordingToPreferredLanguages preferredLanguages: [String]) -> [AVMetadataItem]
```

```objc
+ (NSArray<AVMetadataItem *> *) metadataItemsFromArray:(NSArray<AVMetadataItem *> *) metadataItems filteredAndSortedAccordingToPreferredLanguages:(NSArray<NSString *> *) preferredLanguages;
```

## Return Value

An array of metadata items that match the specified languages.

## Parameters

- `metadataItems`: The metadata items to filter.
- `preferredLanguages`: An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains a canonicalized IETF BCP 47 language identifier. The order of the identifiers in the array reflects the preferred language order, with the most preferred language being first in the array. Typically, you pass the user’s preferred languages by retrieving this array from the [`preferredLanguages`](../../Foundation/nslocale/preferredlanguages.md) class method of [`NSLocale`](../../Foundation/nslocale.md).

## See Also

### Filtering arrays of metadata items
- [class func metadataItems(from: [AVMetadataItem], filteredByIdentifier: AVMetadataIdentifier) -> [AVMetadataItem]](./metadataitems%28from,filteredbyidentifier%29.md)
  Returns metadata items for the specified identifier.
- [class func metadataItems(from: [AVMetadataItem], withKey: Any?, keySpace: AVMetadataKeySpace?) -> [AVMetadataItem]](./metadataitems%28from,withkey,keyspace%29.md)
  Returns metadata items that match a specified key or key space.
- [class func metadataItems(from: [AVMetadataItem], with: Locale) -> [AVMetadataItem]](./metadataitems%28from,with%29.md)
  Returns metadata items that match a specified locale.
- [class func metadataItems(from: [AVMetadataItem], filteredBy: AVMetadataItemFilter) -> [AVMetadataItem]](./metadataitems%28from,filteredby%29.md)
  Returns filtered metadata items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:))*