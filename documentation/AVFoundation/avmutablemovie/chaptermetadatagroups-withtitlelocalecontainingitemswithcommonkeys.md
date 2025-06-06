# chapterMetadataGroups(withTitleLocale:containingItemsWithCommonKeys:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of chapters that contain the specified title locale and common keys.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func chapterMetadataGroups(withTitleLocale locale: Locale, containingItemsWithCommonKeys commonKeys: [AVMetadataKey]?) -> [AVTimedMetadataGroup]
```

#### Return Value

An array of [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) objects.

#### Discussion

A metadata group contains an [`AVMetadataItem`](avmetadataitem.md) object that represents the chapter title, and a time range equal to the time range of the chapter title item.

The system adds a metadata item with the specified common key to an existing [`AVTimedMetadataGroup`](avtimedmetadatagroup.md) object if the time range (timestamp and duration) of the metadata item and the metadata group overlap.

The locale of items that don’t contain chapter titles doesn’t need to match the specified locale parameter. You can filter the returned items based on locale using [`metadataItems(from:with:)`](avmetadataitem/metadataitems(from:with:).md).

## Parameters

- `locale`: The locale of the metadata items carrying chapter titles.
- `commonKeys`: An array of common keys of   to include in the returned array. The framework currently only supports the   key.

## See Also

- [var availableChapterLocales: [Locale]](avmutablemovie/availablechapterlocales.md)
  The locales of the asset’s chapter metadata.
- [func chapterMetadataGroups(bestMatchingPreferredLanguages: [String]) -> [AVTimedMetadataGroup]](avmutablemovie/chaptermetadatagroups(bestmatchingpreferredlanguages:).md)
  Returns an array of chapters with a locale that best matches the list of preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/chaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:))*