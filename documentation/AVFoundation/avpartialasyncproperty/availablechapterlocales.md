# availableChapterLocales

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The locales of an asset’s chapter metadata.

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
static var availableChapterLocales: AVAsyncProperty<Root, [Locale]> { get }
```

Available when `Root` inherits `AVAsset`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading chapter metadata
- [func loadChapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]) async throws -> [AVTimedMetadataGroup]](../avasset/loadchaptermetadatagroups%28withtitlelocale,containingitemswithcommonkeys%29.md)
  Loads chapter metadata that contains the specified title locale and common keys.
- [func loadChapterMetadataGroups(bestMatchingPreferredLanguages: [String], completionHandler: ([AVTimedMetadataGroup]?, (any Error)?) -> Void)](../avasset/loadchaptermetadatagroups%28bestmatchingpreferredlanguages,completionhandler%29.md)
  Loads chapter metadata with a locale that best matches the list of preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availablechapterlocales)*