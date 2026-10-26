# loadChapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:completionHandler:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Loads chapter metadata that contains the specified title locale and common keys.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (void) loadChapterMetadataGroupsWithTitleLocale:(NSLocale *) locale containingItemsWithCommonKeys:(NSArray<NSString *> *) commonKeys completionHandler:(void (^)(NSArray<AVTimedMetadataGroup *> *, NSError *)) completionHandler;
```

## Parameters

- `locale`: The locale of the chapter metadata to load.
- `commonKeys`: An array of common keys of [`AVMetadataItem`](../avmetadataitem.md) to include in the returned array. The framework currently only supports the [`commonKeyArtwork`](../avmetadatakey/commonkeyartwork.md) key.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

  - **metadataGroups**: An array of metadata groups, which may be empty if no groups exist for the locale. The value is `nil` if an error occurs.
  - **error**: An error object if the request fails; otherwise, `nil`.

## See Also

### Loading chapter metadata
- [func loadChapterMetadataGroups(bestMatchingPreferredLanguages: [String], completionHandler: ([AVTimedMetadataGroup]?, (any Error)?) -> Void)](./loadchaptermetadatagroups%28bestmatchingpreferredlanguages,completionhandler%29.md)
  Loads chapter metadata with a locale that best matches the list of preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/loadchaptermetadatagroupswithtitlelocale:containingitemswithcommonkeys:completionhandler:)*