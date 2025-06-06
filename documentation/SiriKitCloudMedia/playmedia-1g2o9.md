# Process a Play Media Intent

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Interpret the user’s request to play a media item, and provide instructions to access a corresponding playback queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

#### Discussion

Processing a play media request requires a few steps:

- Resolve the intended media item.
- Resolve any playback customizations, such as repeat mode.
- Handle the intent.
- Provide a playback queue.

You can improve the overall response time to the user’s request by providing a response for resolving any playback customizations, and handling the intent alongside your response to the request to resolve the intended media item. This allows the client to skip subsequent requests when you can resolve each parameter successfully. If your service responds with a disambiguation, confirmation, or failure, the client disregards the pre-emptive responses, and sends the subsequent intent-processing requests.

## Topics

### Processing a Play Media Intent
- [object PlayMediaIntent](playmediaintent.md)
  An object that describes the user’s request to play a media item.
- [object PlayMediaIntentHandlingInvocation](playmediaintenthandlinginvocation.md)
  A request to process a play media intent.
- [type PlayMediaIntentHandlingInvocationResponse](playmediaintenthandlinginvocationresponse.md)
  The service’s response to a request to process a play media intent.
### Resolving a Media Item
- [object PlayMediaIntentHandlingResolveMediaItemsInvocationResponse](playmediaintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in a play media intent.
- [object PlayMediaMediaItemResolutionResult](playmediamediaitemresolutionresult.md)
  A media item that matches a play media intent, or information about why your service can’t provide a media item.
- [type PlayMediaMediaItemUnsupportedReason](playmediamediaitemunsupportedreason.md)
  Reasons the media service can’t play the media item.
### Handling a Play Media Intent
- [object PlayMediaIntentHandlingHandleInvocationResponse](playmediaintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved play media intent.
- [object PlayMediaIntentResponse](playmediaintentresponse.md)
  A structure that contains a response code indicating how your service handles a play media intent.
- [type PlayMediaIntentResponseCode](playmediaintentresponsecode.md)
  Codes your service can return when handling a play media intent.
### Resolving the Intended Repeat Mode
- [object PlayMediaIntentHandlingResolvePlaybackRepeatModeInvocationResponse](playmediaintenthandlingresolveplaybackrepeatmodeinvocationresponse.md)
  Your service’s response to a request to resolve the repeat mode in a play media intent.
- [object PlayMediaIntentHandlingResolvePlaybackRepeatModeInvocationResponse.Result](playmediaintenthandlingresolveplaybackrepeatmodeinvocationresponse/result-data.dictionary.md)
  The result of resolving the repeat mode for a play media intent.
- [object PlaybackRepeatModeResolutionResult](playbackrepeatmoderesolutionresult.md)
  Information about whether your service can identify the specified repeat mode.
- [type PlaybackRepeatMode](playbackrepeatmode.md)
  The possible repeat modes for a media queue.
### Resolving the Intended Queue Location
- [object PlayMediaIntentHandlingResolvePlaybackQueueLocationInvocationResponse](playmediaintenthandlingresolveplaybackqueuelocationinvocationresponse.md)
  Your service’s response to a request to resolve the queue location in a play media intent.
- [object PlaybackQueueLocationResolutionResult](playbackqueuelocationresolutionresult.md)
  Information about whether your service can resolve the specified queue location.
- [type PlaybackQueueLocation](playbackqueuelocation.md)
  Possible locations in a playback queue to insert a media item.
### Resuming Playback
- [object PlayMediaIntentHandlingResolveResumePlaybackInvocationResponse](playmediaintenthandlingresolveresumeplaybackinvocationresponse.md)
  Your service’s response to a request to resolve whether a play media intent resumes the current playback queue.
### Shuffling Playback
- [object PlayMediaIntentHandlingResolvePlayShuffledInvocationResponse](playmediaintenthandlingresolveplayshuffledinvocationresponse.md)
  Your service’s response to a request to resolve whether a play media intent requests a shuffled queue.

## Request Body

An array of intents to play media.

## See Also

- [Get a Media Queue](playmedia-1onzj.md)
  Provide a playback queue from a successfully processed play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmedia-1g2o9)*