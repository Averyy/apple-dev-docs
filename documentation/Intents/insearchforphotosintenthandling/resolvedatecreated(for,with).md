# resolveDateCreated(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the taken dates for the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveDateCreated(for intent: INSearchForPhotosIntent, with completion: @escaping @Sendable (INDateComponentsRangeResolutionResult) -> Void)
```

```swift
optional func resolveDateCreated(for intent: INSearchForPhotosIntent) async -> INDateComponentsRangeResolutionResult
```

```objc
- (void) resolveDateCreatedForSearchForPhotos:(INSearchForPhotosIntent *) intent withCompletion:(void (^)(INDateComponentsRangeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the taken dates for the phots. When resolving the set of dates, always strive toward a successful resolution, but feel free to ask for confirmation if there’s a date range that you think yields the intended results. For example, if the user asks for photos from Paris taken in June, but your app only has Paris photos from July, you can ask the user to confirm the revised dates.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution with the date range that you’re able to search.

## See Also

### Resolving the Intent Parameters
- [func resolveLocationCreated(for: INSearchForPhotosIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvelocationcreated%28for,with%29.md)
  Resolves the location of the photos.
- [func resolvePeopleInPhoto(for: INSearchForPhotosIntent, with: ([INPersonResolutionResult]) -> Void)](./resolvepeopleinphoto%28for,with%29.md)
  Resolves the people in the photos.
- [func resolveAlbumName(for: INSearchForPhotosIntent, with: (INStringResolutionResult) -> Void)](./resolvealbumname%28for,with%29.md)
  Resolves the name of the photo album containing the photos.
- [func resolveSearchTerms(for: INSearchForPhotosIntent, with: ([INStringResolutionResult]) -> Void)](./resolvesearchterms%28for,with%29.md)
  Resolves any search terms provided by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintenthandling/resolvedatecreated(for:with:))*