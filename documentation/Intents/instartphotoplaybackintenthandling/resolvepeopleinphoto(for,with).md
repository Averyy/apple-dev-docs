# resolvePeopleInPhoto(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the people in the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolvePeopleInPhoto(for intent: INStartPhotoPlaybackIntent, with completion: @escaping @Sendable ([INPersonResolutionResult]) -> Void)
```

```swift
optional func resolvePeopleInPhoto(for intent: INStartPhotoPlaybackIntent) async -> [INPersonResolutionResult]
```

```objc
- (void) resolvePeopleInPhotoForStartPhotoPlayback:(INStartPhotoPlaybackIntent *) intent withCompletion:(void (^)(NSArray<INPersonResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

Implement this method to resolve the people in the photos. Use the information in the `intent` object to locate the corresponding users in your app. Always strive toward a successful resolution of the specified users, but feel free to ask for confirmation for one or more users if there’s some uncertainty.

If you find multiple users matching the same name, consider asking the user to disambiguate from among the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users, consider another resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResults**: The object containing the details of your proposed resolution. For each successful resolution, create a resolution object with the [`INPerson`](../inperson.md) object that you can use to identify the user later.

## See Also

### Resolving the Intent Parameters
- [func resolveDateCreated(for: INStartPhotoPlaybackIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatecreated%28for,with%29.md)
  Resolves the taken dates for the photos.
- [func resolveLocationCreated(for: INStartPhotoPlaybackIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvelocationcreated%28for,with%29.md)
  Resolves the location of the photos.
- [func resolveAlbumName(for: INStartPhotoPlaybackIntent, with: (INStringResolutionResult) -> Void)](./resolvealbumname%28for,with%29.md)
  Resolves the name of the photo album containing the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintenthandling/resolvepeopleinphoto(for:with:))*