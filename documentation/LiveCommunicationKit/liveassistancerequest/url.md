# url

**Framework**: LiveCommunicationKit  
**Kind**: property

The FaceTime-generated URL for this request.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
let url: URL
```

#### Discussion

Forward this URL to your backend in your implementations of [`prepareAssistanceRequest(_:)`](liveassistanceextension/prepareassistancerequest(_:).md) and [`resumeRequest(_:)`](liveassistanceextension/resumerequest(_:).md). When opened, this URL matches an interpreter and joins the call.

FaceTime generates this URL. Your extension only needs to pass it to your backend.

## See Also

- [let id: UUID](liveassistancerequest/id.md)
  A unique identifier that relates the request to a conversation in the FaceTime framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequest/url)*