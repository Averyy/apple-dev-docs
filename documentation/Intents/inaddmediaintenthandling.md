# INAddMediaIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface that adds media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol INAddMediaIntentHandling : NSObjectProtocol
```

```objc
@protocol INAddMediaIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INAddMediaIntentHandling`](./inaddmediaintenthandling.md) protocol to resolve, confirm, and handle requests to add media. Adopt this protocol in an object of your Intents extension that’s capable of adding media.

Siri delivers an [`INAddMediaIntent`](./inaddmediaintent.md) object to your handler when the user asks to add media using your app. Use the methods of this protocol to resolve the parameters and add the media.

## Topics

### Resolving Details of the Intent
- [func resolveMediaDestination(for: INAddMediaIntent, with: (INAddMediaMediaDestinationResolutionResult) -> Void)](./inaddmediaintenthandling/resolvemediadestination%28for,with%29.md)
  Resolves the destination for the added media.
- [func resolveMediaItems(for: INAddMediaIntent, with: ([INAddMediaMediaItemResolutionResult]) -> Void)](./inaddmediaintenthandling/resolvemediaitems%28for,with%29.md)
  Resolves the media items to add.
### Confirming the Response
- [func confirm(intent: INAddMediaIntent, completion: (INAddMediaIntentResponse) -> Void)](./inaddmediaintenthandling/confirm%28intent,completion%29.md)
  Confirms the details of the media addition request.
### Handling the Intent
- [func handle(intent: INAddMediaIntent, completion: (INAddMediaIntentResponse) -> Void)](./inaddmediaintenthandling/handle%28intent,completion%29.md)
  Handles the media addition request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Add Media
- [class INAddMediaIntent](./inaddmediaintent.md)
  A request to add a media item.
- [class INAddMediaIntentResponse](./inaddmediaintentresponse.md)
  An intents handler’s response to an add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintenthandling)*