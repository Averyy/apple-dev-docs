# InvocationResponse

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Properties to include in responses from all intent endpoints.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object InvocationResponse
```

## Topics

### Providing a Result
- [object InvocationResponse.Result](invocationresponse/result-data.dictionary.md)
  The outcome of handling an intent.
### Instrumenting Your Service
- [object ExecutionMetrics](executionmetrics.md)
  Timing information to isolate service performance from network delays.
- [type ServiceDebugReference](servicedebugreference.md)
  A URI that references debugging information for a request.

## Relationships

### Inherited By
- [AddMediaIntentHandlingConfirmInvocationResponse](addmediaintenthandlingconfirminvocationresponse.md)
- [AddMediaIntentHandlingHandleInvocationResponse](addmediaintenthandlinghandleinvocationresponse.md)
- [AddMediaIntentHandlingResolveMediaDestinationInvocationResponse](addmediaintenthandlingresolvemediadestinationinvocationresponse.md)
- [AddMediaIntentHandlingResolveMediaItemsInvocationResponse](addmediaintenthandlingresolvemediaitemsinvocationresponse.md)
- [PlayMediaIntentHandlingHandleInvocationResponse](playmediaintenthandlinghandleinvocationresponse.md)
- [PlayMediaIntentHandlingResolveMediaItemsInvocationResponse](playmediaintenthandlingresolvemediaitemsinvocationresponse.md)
- [PlayMediaIntentHandlingResolvePlayShuffledInvocationResponse](playmediaintenthandlingresolveplayshuffledinvocationresponse.md)
- [PlayMediaIntentHandlingResolvePlaybackQueueLocationInvocationResponse](playmediaintenthandlingresolveplaybackqueuelocationinvocationresponse.md)
- [PlayMediaIntentHandlingResolvePlaybackRepeatModeInvocationResponse](playmediaintenthandlingresolveplaybackrepeatmodeinvocationresponse.md)
- [PlayMediaIntentHandlingResolveResumePlaybackInvocationResponse](playmediaintenthandlingresolveresumeplaybackinvocationresponse.md)
- [ProtocolExceptionInvocationResponse](protocolexceptioninvocationresponse.md)
- [UpdateMediaAffinityIntentHandlingHandleInvocationResponse](updatemediaaffinityintenthandlinghandleinvocationresponse.md)
- [UpdateMediaAffinityIntentHandlingResolveAffinityTypeInvocationResponse](updatemediaaffinityintenthandlingresolveaffinitytypeinvocationresponse.md)
- [UpdateMediaAffinityIntentHandlingResolveMediaItemsInvocationResponse](updatemediaaffinityintenthandlingresolvemediaitemsinvocationresponse.md)

## See Also

- [object Invocation](invocation.md)
  Properties that clients include in requests to all intent endpoints.
- [object Session](session.md)
  Information the client provides about a sequence of requests and responses to process an intent.
- [object Constraints](constraints.md)
  Client-originated limitations on how to process a request, such as including explicit content and how much content the client device can receive in a response.
- [object PlayerContext](playercontext.md)
  Information about the current playback content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/invocationresponse)*