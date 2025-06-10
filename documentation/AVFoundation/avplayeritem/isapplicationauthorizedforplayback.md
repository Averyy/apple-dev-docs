# isApplicationAuthorizedForPlayback

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the application can be used to play the content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
@MainActor
var isApplicationAuthorizedForPlayback: Bool { get }
```

#### Discussion

This property reports whether or not the calling application is authorized to play the content associated with the item.

Application authorization is independent of content authorization (see [`isContentAuthorizedForPlayback`](avplayeritem/iscontentauthorizedforplayback.md)) and that both must be granted in order for an application to be allowed to play protected content. Also, unlike content authorization, application authorization is not dependent on user credentials (that is, if `applicationAuthorizedForPlayback` is [`false`](https://developer.apple.com/documentation/swift/false), there are no means to obtain authorization).

This property is not key-value observable.

## See Also

- [var isContentAuthorizedForPlayback: Bool](avplayeritem/iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](avplayeritem/isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:).md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](avplayeritem/contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [enum AVContentAuthorizationStatus](avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](avplayeritem/cancelcontentauthorizationrequest.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isapplicationauthorizedforplayback)*