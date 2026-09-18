# resumeRequest(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Resumes an assistance request, in response to a call from the framework.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
func resumeRequest(_ request: LiveAssistanceRequest) async throws -> LiveAssistanceRequest.Response
```

#### Discussion

The framework calls this method on your extension after your container app performs any required setup — such as completing a sign in — and calls [`returnToCall(requestID:)`](liveassistance/returntocall(requestid:).md).

In your implementation, do the following:

- Re-perform any needed setup and eligibility checks.
- Forward `request.url` to your backend.
- Return [`LiveAssistanceRequest.Response.proceed`](liveassistancerequest/response/proceed.md). If the request can’t proceed, throw [`LiveAssistanceRequestError`](liveassistancerequesterror.md) instead to end the request.

The framework only calls this method if you handled the original call to [`prepareAssistanceRequest(_:)`](liveassistanceextension/prepareassistancerequest(_:).md) by returning [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](liveassistancerequest/response/requiresuserinput(reason:).md). It doesn’t call this method if you originally returned [`LiveAssistanceRequest.Response.proceed`](liveassistancerequest/response/proceed.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistanceextension/resumerequest(_:))*