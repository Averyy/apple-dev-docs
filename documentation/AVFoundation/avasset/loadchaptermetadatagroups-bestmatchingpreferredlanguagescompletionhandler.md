# loadChapterMetadataGroups(bestMatchingPreferredLanguages:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads chapter metadata with a locale that best matches the list of preferred languages.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func loadChapterMetadataGroups(bestMatchingPreferredLanguages preferredLanguages: [String]) async throws -> [AVTimedMetadataGroup]
```

#### Discussion

This method returns an array of [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) objects asynchronously. Each object in the array contains an [`AVMetadataItem`](avmetadataitem.md) that represents the chapter’s title, and the metadata group’s [`timeRange`](avtimedmetadatagroup/timerange.md) value equals the time range of the chapter title item.

The metadata group contains all chapter metadata, including items with the common key [`commonKeyArtwork`](avmetadatakey/commonkeyartwork.md), if such items are present. The system adds an [`AVMetadataItem`](avmetadataitem.md) with the specified common key to an existing [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap. The locales of such items don’t need to match the locale of the chapter titles.

You can use the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md) method to further filter the metadata items in each group. You can also filter the returned items based on locale using the [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md) method.

## Parameters

- `preferredLanguages`: An array of language identifiers in order of preference, each of which is an IETF BCP 47 (RFC 4646) language identifier. Call    to retrieve the list of languates the user prefers.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var availableChapterLocales: AVAsyncProperty<Root, [Locale]>](avpartialasyncproperty/availablechapterlocales.md)
  The locales of an asset’s chapter metadata.
- [func loadChapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]) async throws -> [AVTimedMetadataGroup]](avasset/loadchaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:).md)
  Loads chapter metadata that contains the specified title locale and common keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/loadchaptermetadatagroups(bestmatchingpreferredlanguages:completionhandler:))*