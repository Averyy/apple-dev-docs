# INUpdateMediaAffinityIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The interface that handles requests to update the user’s preference for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol INUpdateMediaAffinityIntentHandling : NSObjectProtocol
```

```objc
@protocol INUpdateMediaAffinityIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INUpdateMediaAffinityIntentHandling`](./inupdatemediaaffinityintenthandling.md) protocol to resolve, confirm, and handle requests that indicate the user’s preference for a media item. Adopt this protocol in an object of your Intents extension capable of providing feedback for media.

Siri delivers an [`INUpdateMediaAffinityIntent`](./inupdatemediaaffinityintent.md) object to your handler when the user asks to modify their preference for a media item using your app. Use the methods of this protocol to resolve the parameters and update the user’s preference for the media.

## Topics

### Resolving Details of the Intent
- [func resolveAffinityType(for: INUpdateMediaAffinityIntent, with: (INMediaAffinityTypeResolutionResult) -> Void)](./inupdatemediaaffinityintenthandling/resolveaffinitytype%28for,with%29.md)
  Resolves the affinity type to which the media item is updated.
- [func resolveMediaItems(for: INUpdateMediaAffinityIntent, with: ([INUpdateMediaAffinityMediaItemResolutionResult]) -> Void)](./inupdatemediaaffinityintenthandling/resolvemediaitems%28for,with%29.md)
  Resolves the media items for which the user’s preferences are updated.
### Confirming the Response
- [func confirm(intent: INUpdateMediaAffinityIntent, completion: (INUpdateMediaAffinityIntentResponse) -> Void)](./inupdatemediaaffinityintenthandling/confirm%28intent,completion%29.md)
  Confirms the details of the update media affinity request.
### Handling the Intent
- [func handle(intent: INUpdateMediaAffinityIntent, completion: (INUpdateMediaAffinityIntentResponse) -> Void)](./inupdatemediaaffinityintenthandling/handle%28intent,completion%29.md)
  Handles the media update affinity request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Update Media Affinity
- [class INUpdateMediaAffinityIntent](./inupdatemediaaffinityintent.md)
  A request to update the user’s affinity for a media item.
- [class INUpdateMediaAffinityIntentResponse](./inupdatemediaaffinityintentresponse.md)
  An intents handler’s response to an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintenthandling)*