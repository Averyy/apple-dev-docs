# AVContentAuthorizationStatus

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

A value representing the status of a content authorization request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum AVContentAuthorizationStatus
```

```c
enum AVContentAuthorizationStatus : NSInteger;
```

## Overview

Even if authorization is completed by the user, there is no guarantee that the content will then be authorized. You should re-check whether the content is authorized before proceeding.

## Topics

### Content authorization statuses
- [AVContentAuthorizationStatus.unknown](./avcontentauthorizationstatus/unknown.md)
  The content authorization content request hasn’t completed.
- [AVContentAuthorizationStatus.completed](./avcontentauthorizationstatus/completed.md)
  The last completed call to request content authorization completed.
- [AVContentAuthorizationStatus.cancelled](./avcontentauthorizationstatus/cancelled.md)
  The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationStatus.timedOut](./avcontentauthorizationstatus/timedout.md)
  The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationStatus.busy](./avcontentauthorizationstatus/busy.md)
  The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationStatus.notAvailable](./avcontentauthorizationstatus/notavailable.md)
  The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.
- [AVContentAuthorizationStatus.notPossible](./avcontentauthorizationstatus/notpossible.md)
  The last call to request content authorization couldn’t be completed in a non-recoverable way.
### Initializers
- [init?(rawValue: Int)](./avcontentauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing playback authorization in macOS
- [var isContentAuthorizedForPlayback: Bool](./avplayeritem/iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](./avplayeritem/isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [var isApplicationAuthorizedForPlayback: Bool](./avplayeritem/isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](./avplayeritem/requestcontentauthorizationasynchronously%28withtimeoutinterval,completionhandler%29.md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](./avplayeritem/contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [func cancelContentAuthorizationRequest()](./avplayeritem/cancelcontentauthorizationrequest%28%29.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus)*