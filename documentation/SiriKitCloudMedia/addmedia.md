# Process an Add Media Intent

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Add media items to the user’s library or to a playlist.

**Availability**:
- SiriKit Cloud Media 1.0.2+

#### Discussion

Processing a request to add media items to the user’s library or to a playlist requires a few steps: resolving the intended media item, resolving the intended destination library or playlist, confirming the intent, and handling the intent.

You can often improve the overall response time to the user’s request by providing multiple responses to the client’s first request. Include an [`AddMediaIntentHandlingInvocationResponse`](addmediaintenthandlinginvocationresponse.md) for each of the subsequent steps in your response to the first request of a session. This allows the client to skip subsequent requests when you can resolve each parameter successfully. If your service responds with a disambiguation, confirmation, or failure, the client disregards the pre-emptive responses, and sends the subsequent intent-processing requests.

## Topics

### Processing an Add Media Intent
- [object AddMediaIntent](addmediaintent.md)
  An object that describes the user’s request to add media items to their library or to a specific playlist.
- [object AddMediaIntentHandlingInvocation](addmediaintenthandlinginvocation.md)
  A request to process an add media intent.
- [type AddMediaIntentHandlingInvocationResponse](addmediaintenthandlinginvocationresponse.md)
  The service’s response to a request to process an add media intent.
### Identifying a Media Item
- [object AddMediaIntentHandlingResolveMediaItemsInvocationResponse](addmediaintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in an update media affinity intent.
- [object AddMediaMediaItemResolutionResult](addmediamediaitemresolutionresult.md)
  A media item that matches an add media intent, or information about why your service can’t provide a media item.
### Identifying a Library or Playlist
- [object AddMediaIntentHandlingResolveMediaDestinationInvocationResponse](addmediaintenthandlingresolvemediadestinationinvocationresponse.md)
  Your service’s response to a request to resolve media items in an add media intent.
- [object AddMediaMediaDestinationResolutionResult](addmediamediadestinationresolutionresult.md)
  The user’s library or a specified playlist, or information about why your service can’t use the requested destination.
### Confirming and Handling an Add Media Intent
- [object AddMediaIntentResponse](addmediaintentresponse.md)
  A structure that contains a response code indicating your service’s progress in handling an add media intent.
- [type AddMediaIntentResponseCode](addmediaintentresponsecode.md)
  Codes your service can return when confirming or handling an add media intent.
- [object AddMediaIntentHandlingConfirmInvocationResponse](addmediaintenthandlingconfirminvocationresponse.md)
  The service’s response to a request to confirm an add media intent.
- [object AddMediaIntentHandlingHandleInvocationResponse](addmediaintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved add media intent.

## Request Body

An array of requests to process intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmedia)*