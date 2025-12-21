# AVContentAuthorizationStatus

**Framework**: AVFoundation  
**Kind**: enum

A value representing the status of a content authorization request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum AVContentAuthorizationStatus
```

#### Overview

Even if authorization is completed by the user, there is no guarantee that the content will then be authorized. You should re-check whether the content is authorized before proceeding.

## Topics

### Content authorization statuses
- [AVContentAuthorizationStatus.unknown](avcontentauthorizationstatus/unknown.md)
  The content authorization content request hasn’t completed.
- [AVContentAuthorizationStatus.completed](avcontentauthorizationstatus/completed.md)
  The last completed call to request content authorization completed.
- [AVContentAuthorizationStatus.cancelled](avcontentauthorizationstatus/cancelled.md)
  The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationStatus.timedOut](avcontentauthorizationstatus/timedout.md)
  The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationStatus.busy](avcontentauthorizationstatus/busy.md)
  The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationStatus.notAvailable](avcontentauthorizationstatus/notavailable.md)
  The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.
- [AVContentAuthorizationStatus.notPossible](avcontentauthorizationstatus/notpossible.md)
  The last call to request content authorization couldn’t be completed in a non-recoverable way.
### Initializers
- [init?(rawValue: Int)](avcontentauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isContentAuthorizedForPlayback: Bool](avplayeritem/iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](avplayeritem/isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [var isApplicationAuthorizedForPlayback: Bool](avplayeritem/isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:).md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](avplayeritem/contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [func cancelContentAuthorizationRequest()](avplayeritem/cancelcontentauthorizationrequest.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus)*