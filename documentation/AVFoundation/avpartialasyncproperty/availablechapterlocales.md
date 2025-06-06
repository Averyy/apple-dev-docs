# availableChapterLocales

**Framework**: AVFoundation  
**Kind**: property

The locales of an asset’s chapter metadata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var availableChapterLocales: AVAsyncProperty<Root, [Locale]> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

## See Also

- [func loadChapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]) async throws -> [AVTimedMetadataGroup]](avasset/loadchaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:).md)
  Loads chapter metadata that contains the specified title locale and common keys.
- [func loadChapterMetadataGroups(bestMatchingPreferredLanguages: [String], completionHandler: ([AVTimedMetadataGroup]?, (any Error)?) -> Void)](avasset/loadchaptermetadatagroups(bestmatchingpreferredlanguages:completionhandler:).md)
  Loads chapter metadata with a locale that best matches the list of preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availablechapterlocales)*