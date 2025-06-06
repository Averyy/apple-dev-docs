# availableChapterLocales

**Framework**: AVFoundation  
**Kind**: property

The locales of the asset’s chapter metadata.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var availableChapterLocales: [Locale] { get }
```

## See Also

- [func chapterMetadataGroups(bestMatchingPreferredLanguages: [String]) -> [AVTimedMetadataGroup]](avcomposition/chaptermetadatagroups(bestmatchingpreferredlanguages:).md)
  Returns an array of chapters with a locale that best matches the list of preferred languages.
- [func chapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]?) -> [AVTimedMetadataGroup]](avcomposition/chaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:).md)
  Returns an array of chapters that contain the specified title locale and common keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/availablechapterlocales)*