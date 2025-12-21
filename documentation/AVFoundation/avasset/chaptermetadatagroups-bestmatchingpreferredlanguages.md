# chapterMetadataGroups(bestMatchingPreferredLanguages:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of chapters with a locale that best matches the list of preferred languages.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func chapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) -> [AVTimedMetadataGroup]
```

## Mentions

- [Presenting chapter markers](presenting-chapter-markers.md)

#### Return Value

An array of [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) objects.

#### Discussion

Each object in the returned array contains an [`AVMetadataItem`](avmetadataitem.md) object representing the chapter title. The time range property of the [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) object is equal to the time range of the chapter title item.

The metadata group contains all chapter metadata, including items with the common key [`commonKeyArtwork`](avmetadatakey/commonkeyartwork.md), if such items are present. The system adds an [`AVMetadataItem`](avmetadataitem.md) with the specified common key to an existing [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap. The locale of such items don’t need to match the locale of the chapter titles.

You can use the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md) method to further filter the metadata items in each group. You can also filter the returned items based on locale using the [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md) method.

This method is callable without blocking the current thread after you’ve asynchronously loaded the [`availableChapterLocales`](avasset/availablechapterlocales.md) property.

## Parameters

- `preferredLanguages`: An array of BCP 47 language identifier strings. The order of the identifiers in the array reflects the preferred language order, with the most preferred language being first in the array. Typically, you pass the user’s preferred languages by retrieving this array from the   class method of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/chaptermetadatagroups(bestmatchingpreferredlanguages:))*