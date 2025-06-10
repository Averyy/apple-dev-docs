# isContentAuthorizedForPlayback

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the content has been authorized by the user.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
@MainActor
var isContentAuthorizedForPlayback: Bool { get }
```

#### Discussion

This property reports whether the user has provided the necessary credentials to the system in order for the content to be decrypted for playback.

Content authorization is independent of application authorization (see [`isApplicationAuthorizedForPlayback`](avplayeritem/isapplicationauthorizedforplayback.md)) and that both must be granted in order for an application to be allowed to play protected content.

This property is not key-value observable.

## See Also

- [var isAuthorizationRequiredForPlayback: Bool](avplayeritem/isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [var isApplicationAuthorizedForPlayback: Bool](avplayeritem/isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:).md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](avplayeritem/contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [enum AVContentAuthorizationStatus](avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](avplayeritem/cancelcontentauthorizationrequest.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/iscontentauthorizedforplayback)*