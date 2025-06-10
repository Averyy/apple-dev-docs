# processContentKeyResponse(_:)

**Framework**: AVFoundation  
**Kind**: method

Sends the specified content key response to the receiver for processing.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func processContentKeyResponse(_ keyResponse: AVContentKeyResponse)
```

#### Discussion

After receiving a content key request and calling [`makeStreamingContentKeyRequestData(forApp:contentIdentifier:options:completionHandler:)`](avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp:contentidentifier:options:completionhandler:).md) on that request, you must obtain a response to the request in accordance with the protocol used by the entity that controls the use of the media data. Use this method to provide the content key response, to make protected content available for processing.

## Parameters

- `keyResponse`: An   object carrying a response to a content key request.

## See Also

- [func respondByRequestingPersistableContentKeyRequest()](avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest-1ci4q.md)
  Tells the receiver that the app requires a persistable content key request object for processing.
- [func processContentKeyResponseError(any Error)](avcontentkeyrequest/processcontentkeyresponseerror(_:).md)
  Tells the receiver that the app was unable to obtain a content key response.
- [func respondByRequestingPersistableContentKeyRequest()](avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest-1ci4q.md)
  Tells the receiver that the app requires a persistable content key request object for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponse(_:))*