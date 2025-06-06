# requestContentAuthorizationAsynchronously(withTimeoutInterval:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Presents the user the opportunity to authorize the content for playback.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func requestContentAuthorization(withTimeoutInterval timeoutInterval: TimeInterval) async
```

#### Discussion

Calling this method will present the user with the opportunity to authorize the content (for example, by launching iTunes and prompting the user to enter their Apple ID and password).

When the user has taken action (or the timeout has elapsed), the completion handler is invoked. You determine the status of the authorization attempt by checking the value of the [`contentAuthorizationRequestStatus`](avplayeritem/contentauthorizationrequeststatus.md) property.

Even if the status indicates a completed authorization, the content may still not be authorized (for example, if the user authorizes an Apple ID other than that associated with the content).  You should re-check the value of [`contentAuthorizationRequestStatus`](avplayeritem/contentauthorizationrequeststatus.md) to verify whether the content has actually been authorized before continuing.  It is not necessary to call this method if the value of [`contentAuthorizationRequestStatus`](avplayeritem/contentauthorizationrequeststatus.md) is already true.

## Parameters

- `timeoutInterval`: The maximum amount of time in seconds to wait for the user to authorize the content before calling the handler block with a timeout result.
- `handler`: The block to be called upon completion.

## See Also

- [var isContentAuthorizedForPlayback: Bool](avplayeritem/iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](avplayeritem/isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [var isApplicationAuthorizedForPlayback: Bool](avplayeritem/isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](avplayeritem/contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [enum AVContentAuthorizationStatus](avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](avplayeritem/cancelcontentauthorizationrequest.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:))*