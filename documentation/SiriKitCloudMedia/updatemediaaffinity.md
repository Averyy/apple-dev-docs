# Process an Update Media Affinity Intent

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Record the user’s preference for a specific media item or a broader category of media.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Topics

### Processing an Update Media Affinity Intent
- [object UpdateMediaAffinityIntent](updatemediaaffinityintent.md)
  An object that describes a user’s stated preference regarding media items.
- [object UpdateMediaAffinityIntentHandlingInvocation](updatemediaaffinityintenthandlinginvocation.md)
  A request to process an update media affinity intent.
- [type UpdateMediaAffinityIntentHandlingInvocationResponse](updatemediaaffinityintenthandlinginvocationresponse.md)
  The service’s response to a request to process an update media affinity intent.
### Identifying the Intended Media Items
- [object UpdateMediaAffinityIntentHandlingResolveMediaItemsInvocationResponse](updatemediaaffinityintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in an update media affinity intent.
- [object UpdateMediaAffinityMediaItemResolutionResult](updatemediaaffinitymediaitemresolutionresult.md)
  A media item that matches an update media affinity intent, or information about why your service can’t provide a media item.
- [type UpdateMediaAffinityMediaItemUnsupportedReason](updatemediaaffinitymediaitemunsupportedreason.md)
  Reasons the media service can’t update information about the media item.
### Discerning Like or Dislike
- [type MediaAffinityType](mediaaffinitytype.md)
  A preference or dislike for a media item.
- [object UpdateMediaAffinityIntentHandlingResolveAffinityTypeInvocationResponse](updatemediaaffinityintenthandlingresolveaffinitytypeinvocationresponse.md)
  Your service’s response to a request that expresses a preference or dislike for a media item.
- [object MediaAffinityTypeResolutionResult](mediaaffinitytyperesolutionresult.md)
  A media affinity that matches an update media affinity intent, or information about why your service can’t determine the media affinity.
### Handling an Update Media Affinity Intent
- [object UpdateMediaAffinityIntentHandlingHandleInvocationResponse](updatemediaaffinityintenthandlinghandleinvocationresponse.md)
  Your service’s response to a request to handle a fully resolved update media affinity intent.
- [object UpdateMediaAffinityIntentResponse](updatemediaaffinityintentresponse.md)
  A structure that contains a response code indicating how your service handles an update media affinity intent.
- [type UpdateMediaAffinityIntentResponseCode](updatemediaaffinityintentresponsecode.md)
  Codes your service can return when handling an update media affinity intent.

## Endpoint

`POST https://cloudextension-testservice.local/api/intent/updateMediaAffinity`

## Parameters

- `Accept-Language` (string) *(required)*: The client’s current user interface language. Respond with localized content for this language, if available.
- `Request-Timeout` (uint32) *(required)*: An approximate deadline, in seconds, for processing this real-time user request. The [`Session`](session.md) object provides the exact deadline for handling an intent.
- `User-Agent` (string) *(required)*: The extension protocol running on the client. This is an RFC 7231-compliant string that contains the product name *AppleCloudExtension* and the SiriKit Extension library version running on the client.
- `x-applecloudextension-retry-count` (uint32): The number of previous requests from the client. The client omits this header on the first attempt.
- `x-applecloudextension-session-id` (string) *(required)*: A constant session identifier to include in each request and response. Respond to each request with the session ID the client sends in that request.

## Request Body

An array of requests to process intents.

## See Also

- [type QueueActivityReportEvent](queueactivityreportevent.md)
  An event that occurs during content playback.
- [Report Playback Progress and Activity](updateactivity.md)
  Monitor progress through the playback queue.
- [object UpdateActivityRequest](updateactivityrequest.md)
  A report of the client’s current playback state and recent user interaction, and an opportunity for your service to modify the client’s playback queue.
- [object UpdateActivityResponse](updateactivityresponse.md)
  Updates to the client’s queue and user activity in response to a report of playback progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinity)*