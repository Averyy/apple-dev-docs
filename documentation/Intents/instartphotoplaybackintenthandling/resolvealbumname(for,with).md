# resolveAlbumName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the name of the photo album containing the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveAlbumName(for intent: INStartPhotoPlaybackIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveAlbumName(for intent: INStartPhotoPlaybackIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveAlbumNameForStartPhotoPlayback:(INStartPhotoPlaybackIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the name of the photo album.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the album name that you intend to use during the search.

## See Also

### Resolving the Intent Parameters
- [func resolveDateCreated(for: INStartPhotoPlaybackIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatecreated%28for,with%29.md)
  Resolves the taken dates for the photos.
- [func resolveLocationCreated(for: INStartPhotoPlaybackIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvelocationcreated%28for,with%29.md)
  Resolves the location of the photos.
- [func resolvePeopleInPhoto(for: INStartPhotoPlaybackIntent, with: ([INPersonResolutionResult]) -> Void)](./resolvepeopleinphoto%28for,with%29.md)
  Resolves the people in the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintenthandling/resolvealbumname(for:with:))*