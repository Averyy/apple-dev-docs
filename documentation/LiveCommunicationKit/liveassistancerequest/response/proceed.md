# LiveAssistanceRequest.Response.proceed

**Framework**: LiveCommunicationKit  
**Kind**: case

A response that indicates the extension successfully handled the request and setting up live assistance can proceed.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
case proceed
```

#### Discussion

When you return this value, FaceTime displays a “waiting” tile while your service finds a match.

Prior to returning this value, forward [`url`](liveassistancerequest/url.md) to your backend.

## See Also

- [case requiresUserInput(reason: LiveAssistanceLaunchReason)](liveassistancerequest/response/requiresuserinput(reason:).md)
  A response that indicates the extension needs to complete a task in the container app before the request can proceed.
- [enum LiveAssistanceLaunchReason](liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequest/response/proceed)*