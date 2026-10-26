# INStartPhotoPlaybackIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for searching the user’s photos and the playback of the results.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INStartPhotoPlaybackIntentHandling : NSObjectProtocol
```

```objc
@protocol INStartPhotoPlaybackIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INStartPhotoPlaybackIntentHandling`](./instartphotoplaybackintenthandling.md) protocol to resolve, confirm, and handle requests to search the user’s photos and initiate playback of a slideshow. Adopt this protocol in an object of your Intents extension that’s capable of performing the search and determining the number of results. Siri doesn’t display the photos found during the search. After a successful search, Siri launches your app so that it can begin the slideshow.

Siri delivers an [`INStartPhotoPlaybackIntent`](./instartphotoplaybackintent.md) object to your handler when the user asks to start a slideshow. The provided intent object contains the search parameters to use for matching photos to include in the slideshow. Use the methods of this protocol to resolve the search parameters, to perform the search, and to return the number of photos that match the criteria.

## Topics

### Resolving the Intent Parameters
- [func resolveDateCreated(for: INStartPhotoPlaybackIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./instartphotoplaybackintenthandling/resolvedatecreated%28for,with%29.md)
  Resolves the taken dates for the photos.
- [func resolveLocationCreated(for: INStartPhotoPlaybackIntent, with: (INPlacemarkResolutionResult) -> Void)](./instartphotoplaybackintenthandling/resolvelocationcreated%28for,with%29.md)
  Resolves the location of the photos.
- [func resolvePeopleInPhoto(for: INStartPhotoPlaybackIntent, with: ([INPersonResolutionResult]) -> Void)](./instartphotoplaybackintenthandling/resolvepeopleinphoto%28for,with%29.md)
  Resolves the people in the photos.
- [func resolveAlbumName(for: INStartPhotoPlaybackIntent, with: (INStringResolutionResult) -> Void)](./instartphotoplaybackintenthandling/resolvealbumname%28for,with%29.md)
  Resolves the name of the photo album containing the photos.
### Confirming the Response
- [func confirm(intent: INStartPhotoPlaybackIntent, completion: (INStartPhotoPlaybackIntentResponse) -> Void)](./instartphotoplaybackintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can perform the search.
### Handling the Intent
- [func handle(intent: INStartPhotoPlaybackIntent, completion: (INStartPhotoPlaybackIntentResponse) -> Void)](./instartphotoplaybackintenthandling/handle%28intent,completion%29.md)
  Handles performing the search and returning the number of results.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPhotosDomainHandling](./inphotosdomainhandling.md)

## See Also

### Photo Playback
- [class INStartPhotoPlaybackIntent](./instartphotoplaybackintent.md)
  A request to search for photos and initiate a slideshow with the results.
- [class INStartPhotoPlaybackIntentResponse](./instartphotoplaybackintentresponse.md)
  Your app’s response to a start photo playback intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintenthandling)*