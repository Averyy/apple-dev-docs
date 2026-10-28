# resumeRequest(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Resumes an assistance request, in response to a call from the framework.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
@MainActor
func resumeRequest(_ request: LiveAssistanceRequest) async throws -> LiveAssistanceRequest.Response
```

## Discussion

The framework calls this method on your extension after your container app performs any required setup — such as completing a sign in — and calls [`returnToCall(requestID:)`](../liveassistance/returntocall%28requestid%29.md).

In your implementation, do the following:

- Re-perform any needed setup and eligibility checks.
- Forward `request.url` to your backend.
- Return [`LiveAssistanceRequest.Response.proceed`](../liveassistancerequest/response/proceed.md). If the request can’t proceed, throw [`LiveAssistanceRequestError`](../liveassistancerequesterror.md) instead to end the request.

The framework only calls this method if you handled the original call to [`prepareAssistanceRequest(_:)`](./prepareassistancerequest%28_%29.md) by returning [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](../liveassistancerequest/response/requiresuserinput%28reason%29.md). It doesn’t call this method if you originally returned [`LiveAssistanceRequest.Response.proceed`](../liveassistancerequest/response/proceed.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistanceextension/resumerequest(_:))*