# availableChapterLocales

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The locales of the asset’s chapter metadata.

**Availability**:
- iOS 4.3+ - Deprecated in 16.0
- iPadOS 4.3+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`availableChapterLocales`](../avpartialasyncproperty/availablechapterlocales.md) asynchronously instead.

## Declaration

```swift
var availableChapterLocales: [Locale] { get }
```

```objc
@property (readonly) NSArray<NSLocale *> * availableChapterLocales;
```

## Mentions

- [Presenting chapter markers](../presenting-chapter-markers.md)

## See Also

### Accessing chapter metadata
- [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](./chaptermetadatagroups%28withtitlelocale,containingitemswithcommonkeys%29.md)
  Returns an array of chapters that contain the specified title locale and common keys.
- [- chapterMetadataGroupsBestMatchingPreferredLanguages:](./chaptermetadatagroups%28bestmatchingpreferredlanguages%29.md)
  Returns an array of chapters with a locale that best matches the list of preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/availablechapterlocales)*