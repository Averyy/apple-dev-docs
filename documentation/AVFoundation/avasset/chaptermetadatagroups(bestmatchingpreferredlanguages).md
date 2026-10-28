# chapterMetadataGroups(bestMatchingPreferredLanguages:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of chapters with a locale that best matches the list of preferred languages.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadChapterMetadataGroups(bestMatchingPreferredLanguages:completionHandler:)`](./loadchaptermetadatagroups%28bestmatchingpreferredlanguages,completionhandler%29.md) instead.

## Declaration

```swift
func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup]
```

```objc
- (NSArray<AVTimedMetadataGroup *> *) chapterMetadataGroupsBestMatchingPreferredLanguages:(NSArray<NSString *> *) preferredLanguages;
```

## Mentions

- [Presenting chapter markers](../presenting-chapter-markers.md)

## Return Value

An array of [`AVTimedMetadataGroup`](../avtimedmetadatagroup.md) objects.

## Discussion

Each object in the returned array contains an [`AVMetadataItem`](../avmetadataitem.md) object representing the chapter title. The time range property of the [`AVTimedMetadataGroup`](../avtimedmetadatagroup.md) object is equal to the time range of the chapter title item.

The metadata group contains all chapter metadata, including items with the common key [`commonKeyArtwork`](../avmetadatakey/commonkeyartwork.md), if such items are present. The system adds an [`AVMetadataItem`](../avmetadataitem.md) with the specified common key to an existing [`AVTimedMetadataGroup`](../avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap. The locale of such items don’t need to match the locale of the chapter titles.

You can use the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](../avmetadataitem/metadataitems%28from,filteredandsortedaccordingtopreferredlanguages%29.md) method to further filter the metadata items in each group. You can also filter the returned items based on locale using the [`metadataItems(from:with:)`](../avmetadataitem/metadataitems%28from,with%29.md) method.

This method is callable without blocking the current thread after you’ve asynchronously loaded the [`availableChapterLocales`](./availablechapterlocales.md) property.

## Parameters

- `preferredLanguages`: An array of BCP 47 language identifier strings. The order of the identifiers in the array reflects the preferred language order, with the most preferred language being first in the array. Typically, you pass the user’s preferred languages by retrieving this array from the [`preferredLanguages`](../../Foundation/nslocale/preferredlanguages.md) class method of [`NSLocale`](../../Foundation/nslocale.md).

## See Also

### Accessing chapter metadata
- [availableChapterLocales](./availablechapterlocales.md)
  The locales of the asset’s chapter metadata.
- [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](./chaptermetadatagroups%28withtitlelocale,containingitemswithcommonkeys%29.md)
  Returns an array of chapters that contain the specified title locale and common keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/chaptermetadatagroups(bestmatchingpreferredlanguages:))*