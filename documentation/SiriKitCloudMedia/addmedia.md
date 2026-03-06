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

## Endpoint

`POST https://cloudextension-testservice.local/api/intent/addMedia`

## Parameters

- `Accept-Language` (string) *(required)*: The client’s current user interface language. Respond with localized content for this language, if available.
- `Request-Timeout` (uint32) *(required)*: An approximate deadline, in seconds, for processing this real-time user request. The [`Session`](session.md) object provides the exact deadline for handling an intent.
- `User-Agent` (string) *(required)*: The extension protocol running on the client. This is an RFC 7231-compliant string that contains the product name *AppleCloudExtension* and the SiriKit Extension library version running on the client.
- `x-applecloudextension-retry-count` (uint32): The number of previous requests from the client.
- `x-applecloudextension-session-id` (string) *(required)*: A constant session identifier to include in each request and response. Respond to each request with the same session ID the client sends in that request.

## Request Body

An array of requests to process intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmedia)*