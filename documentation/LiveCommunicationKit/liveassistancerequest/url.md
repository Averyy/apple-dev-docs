# url

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Instance Property

The FaceTime-generated URL for this request.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
let url: URL
```

#### Discussion

Forward this URL to your backend in your implementations of [`prepareAssistanceRequest(_:)`](../liveassistanceextension/prepareassistancerequest%28_%29.md) and [`resumeRequest(_:)`](../liveassistanceextension/resumerequest%28_%29.md). When opened, this URL matches an interpreter and joins the call.

FaceTime generates this URL. Your extension only needs to pass it to your backend.

## See Also

### Working with request properties
- [let id: UUID](./id.md)
  A unique identifier that relates the request to a conversation in the FaceTime framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancerequest/url)*