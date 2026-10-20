# LiveAssistanceRequest.Response.proceed

**Framework**: LiveCommunicationKit  
**Kind**: case  
**Role**: Case

A response that indicates the extension successfully handled the request and setting up live assistance can proceed.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
case proceed
```

#### Discussion

When you return this value, FaceTime displays a “waiting” tile while your service finds a match.

Prior to returning this value, forward [`url`](../url.md) to your backend.

## See Also

### Working with responses
- [case requiresUserInput(reason: LiveAssistanceLaunchReason)](./requiresuserinput%28reason%29.md)
  A response that indicates the extension needs to complete a task in the container app before the request can proceed.
- [enum LiveAssistanceLaunchReason](../../liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequest/response/proceed)*