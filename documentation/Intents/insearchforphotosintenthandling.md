# INSearchForPhotosIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for searching the user’s photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INSearchForPhotosIntentHandling : NSObjectProtocol
```

```objc
@protocol INSearchForPhotosIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSearchForPhotosIntentHandling`](./insearchforphotosintenthandling.md) protocol to resolve, confirm, and handle requests to search the photos in your app. Adopt this protocol in an object of your Intents extension that’s capable of performing the search and determining the number of results. Siri doesn’t display the photos found during the search. After a successful search, Siri launches your app to display the photos.

Siri delivers an [`INSearchForPhotosIntent`](./insearchforphotosintent.md) object to your handler when the user asks to search their photos. The provided intent object contains the parameters to use when searching for the photos. Use the methods of this protocol to resolve the search parameters, to perform the search, and to return the number of photos that match the criteria.

## Topics

### Resolving the Intent Parameters
- [func resolveDateCreated(for: INSearchForPhotosIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./insearchforphotosintenthandling/resolvedatecreated%28for,with%29.md)
  Resolves the taken dates for the photos.
- [func resolveLocationCreated(for: INSearchForPhotosIntent, with: (INPlacemarkResolutionResult) -> Void)](./insearchforphotosintenthandling/resolvelocationcreated%28for,with%29.md)
  Resolves the location of the photos.
- [func resolvePeopleInPhoto(for: INSearchForPhotosIntent, with: ([INPersonResolutionResult]) -> Void)](./insearchforphotosintenthandling/resolvepeopleinphoto%28for,with%29.md)
  Resolves the people in the photos.
- [func resolveAlbumName(for: INSearchForPhotosIntent, with: (INStringResolutionResult) -> Void)](./insearchforphotosintenthandling/resolvealbumname%28for,with%29.md)
  Resolves the name of the photo album containing the photos.
- [func resolveSearchTerms(for: INSearchForPhotosIntent, with: ([INStringResolutionResult]) -> Void)](./insearchforphotosintenthandling/resolvesearchterms%28for,with%29.md)
  Resolves any search terms provided by the user.
### Confirming the Response
- [func confirm(intent: INSearchForPhotosIntent, completion: (INSearchForPhotosIntentResponse) -> Void)](./insearchforphotosintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can perform the search.
### Handling the Intent
- [func handle(intent: INSearchForPhotosIntent, completion: (INSearchForPhotosIntentResponse) -> Void)](./insearchforphotosintenthandling/handle%28intent,completion%29.md)
  Handles searching the photos and returning the number of results.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INPhotosDomainHandling](./inphotosdomainhandling.md)

## See Also

### Photo Search
- [class INSearchForPhotosIntent](./insearchforphotosintent.md)
  A request for the list of photos that match the specified criteria.
- [class INSearchForPhotosIntentResponse](./insearchforphotosintentresponse.md)
  Your app’s response to a search for photos intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintenthandling)*