# INPlayMediaIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The interface an object implements to confirm and handle play media intents.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
protocol INPlayMediaIntentHandling : NSObjectProtocol
```

```objc
@protocol INPlayMediaIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INPlayMediaIntentHandling`](./inplaymediaintenthandling.md) protocol to confirm and handle requests for media playback in your app. Adopt this protocol in an object of your Intents app extension capable of verifying that the media is playable in your app. When handling the playback request, send the request to your app and let your app perform the playback, rather than playing the media in the extension. The lifespan of extensions is too short for media playback.

Siri delivers an [`INPlayMediaIntent`](./inplaymediaintent.md) object to your handler when the user invokes the media intent shortcut. This intent object contains metadata that identifies the requested media content.

## Topics

### Resolving the Intent Parameters
- [func resolveMediaItems(for: INPlayMediaIntent, with: ([INPlayMediaMediaItemResolutionResult]) -> Void)](./inplaymediaintenthandling/resolvemediaitems%28for,with%29.md)
  Resolves the media items to play.
- [func resolvePlayShuffled(for: INPlayMediaIntent, with: (INBooleanResolutionResult) -> Void)](./inplaymediaintenthandling/resolveplayshuffled%28for,with%29.md)
  Resolves whether to shuffle the played media.
- [func resolvePlaybackQueueLocation(for: INPlayMediaIntent, with: (INPlaybackQueueLocationResolutionResult) -> Void)](./inplaymediaintenthandling/resolveplaybackqueuelocation%28for,with%29.md)
  Resolves the location in the playback queue where your app plays the media.
- [func resolvePlaybackRepeatMode(for: INPlayMediaIntent, with: (INPlaybackRepeatModeResolutionResult) -> Void)](./inplaymediaintenthandling/resolveplaybackrepeatmode%28for,with%29.md)
  Resolves the repeat mode when playing media.
- [func resolvePlaybackSpeed(for: INPlayMediaIntent, with: (INPlayMediaPlaybackSpeedResolutionResult) -> Void)](./inplaymediaintenthandling/resolveplaybackspeed%28for,with%29.md)
  Resolves the playback speed when playing media.
- [func resolveResumePlayback(for: INPlayMediaIntent, with: (INBooleanResolutionResult) -> Void)](./inplaymediaintenthandling/resolveresumeplayback%28for,with%29.md)
  Resolves whether to resume playback.
### Confirming the Intent
- [func confirm(intent: INPlayMediaIntent, completion: (INPlayMediaIntentResponse) -> Void)](./inplaymediaintenthandling/confirm%28intent,completion%29.md)
  Confirms the details of the media playback request.
### Handling the Intent
- [func handle(intent: INPlayMediaIntent, completion: (INPlayMediaIntentResponse) -> Void)](./inplaymediaintenthandling/handle%28intent,completion%29.md)
  Handles the media playback request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Playable Media Intents
- [class INPlayMediaIntent](./inplaymediaintent.md)
  An intent that contains information about media playable from your app.
- [class INPlayMediaIntentResponse](./inplaymediaintentresponse.md)
  An intents handler’s response to a play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintenthandling)*