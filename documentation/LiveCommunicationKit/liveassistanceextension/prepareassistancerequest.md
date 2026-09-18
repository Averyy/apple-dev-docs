# prepareAssistanceRequest(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Prepares to handle a fresh assistance request, in response to a call from the framework.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
func prepareAssistanceRequest(_ request: LiveAssistanceRequest) async throws -> LiveAssistanceRequest.Response
```

#### Discussion

Implement this method by performing any necessarily setup and eligibility checks. When finished, do one of the following:

- If the request can proceed, forward `request.url` to your backend, and return [`LiveAssistanceRequest.Response.proceed`](liveassistancerequest/response/proceed.md). In this scenario, this is the only method your extension handles, because the framework doesn’t need to call [`resumeRequest(_:)`](liveassistanceextension/resumerequest(_:).md).
- If the request requires logging in or other interaction from the person using the app, return [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](liveassistancerequest/response/requiresuserinput(reason:).md) to transfer control to your container app.
- If the request can’t proceed, throw a [`LiveAssistanceRequestError`](liveassistancerequesterror.md) to end the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistanceextension/prepareassistancerequest(_:))*