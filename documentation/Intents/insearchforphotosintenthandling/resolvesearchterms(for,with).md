# resolveSearchTerms(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves any search terms provided by the user.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveSearchTerms(for intent: INSearchForPhotosIntent, with completion: @escaping @Sendable ([INStringResolutionResult]) -> Void)
```

```swift
optional func resolveSearchTerms(for intent: INSearchForPhotosIntent) async -> [INStringResolutionResult]
```

```objc
- (void) resolveSearchTermsForSearchForPhotos:(INSearchForPhotosIntent *) intent withCompletion:(void (^)(NSArray<INStringResolutionResult *> *resolutionResults)) completion;
```

## Discussion

Implement this method to resolve any search terms provided by the user.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the terms that you intend to use during the search.

## See Also

### Resolving the Intent Parameters
- [func resolveDateCreated(for: INSearchForPhotosIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatecreated%28for,with%29.md)
  Resolves the taken dates for the photos.
- [func resolveLocationCreated(for: INSearchForPhotosIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvelocationcreated%28for,with%29.md)
  Resolves the location of the photos.
- [func resolvePeopleInPhoto(for: INSearchForPhotosIntent, with: ([INPersonResolutionResult]) -> Void)](./resolvepeopleinphoto%28for,with%29.md)
  Resolves the people in the photos.
- [func resolveAlbumName(for: INSearchForPhotosIntent, with: (INStringResolutionResult) -> Void)](./resolvealbumname%28for,with%29.md)
  Resolves the name of the photo album containing the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintenthandling/resolvesearchterms(for:with:))*