# INSearchForMediaIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The interface that handles media search requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol INSearchForMediaIntentHandling : NSObjectProtocol
```

```objc
@protocol INSearchForMediaIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INSearchForMediaIntentHandling`](./insearchformediaintenthandling.md) protocol to resolve, confirm, and handle requests to search for media. Adopt this protocol in an object of your Intents extension capable of searching for media.

Siri delivers an [`INSearchForMediaIntent`](./insearchformediaintent.md) object to your handler when the user asks Siri to search for media using your app, or when Spotlight search results include an artist. Use the methods of this protocol to resolve the parameters and search for the media.

## Topics

### Resolving Details of the Intent
- [func resolveMediaItems(for: INSearchForMediaIntent, with: ([INSearchForMediaMediaItemResolutionResult]) -> Void)](./insearchformediaintenthandling/resolvemediaitems%28for,with%29.md)
  Resolves the media items for which to search.
### Confirming the Response
- [func confirm(intent: INSearchForMediaIntent, completion: (INSearchForMediaIntentResponse) -> Void)](./insearchformediaintenthandling/confirm%28intent,completion%29.md)
  Confirms the details of the media search request.
### Handling the Intent
- [func handle(intent: INSearchForMediaIntent, completion: (INSearchForMediaIntentResponse) -> Void)](./insearchformediaintenthandling/handle%28intent,completion%29.md)
  Handles the media search request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Search for Media
- [class INSearchForMediaIntent](./insearchformediaintent.md)
  A request to search for a media item.
- [class INSearchForMediaIntentResponse](./insearchformediaintentresponse.md)
  An intents handler’s response to a search media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintenthandling)*