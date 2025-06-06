# cancelContentAuthorizationRequest()

**Framework**: AVFoundation  
**Kind**: method

Cancels the currently outstanding content authorization request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func cancelContentAuthorizationRequest()
```

#### Discussion

Calling this method while a content authorization request is pending will cause that request to be cancelled and its completion handler to be invoked with a status of [`AVContentAuthorizationStatus.cancelled`](avcontentauthorizationstatus/cancelled.md).

This method does not block.

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
- [enum AVContentAuthorizationStatus](avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/cancelcontentauthorizationrequest())*