# contentAuthorizationRequestStatus

**Framework**: AVFoundation  
**Kind**: property

The status of the most recent content authorization request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var contentAuthorizationRequestStatus: AVContentAuthorizationStatus { get }
```

#### Discussion

This property reports the authorization status as determined by the most recent call to [`requestContentAuthorizationAsynchronously(withTimeoutInterval:completionHandler:)`](avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:).md).

The value will be [`AVContentAuthorizationStatus.unknown`](avcontentauthorizationstatus/unknown.md) before the first call and between the time a request call is made and just prior to the completion handler being executed (thus it is safe to query this property from the completion handler).

This value is not key-value observable.

## See Also

- [var isContentAuthorizedForPlayback: Bool](avplayeritem/iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](avplayeritem/isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [var isApplicationAuthorizedForPlayback: Bool](avplayeritem/isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](avplayeritem/requestcontentauthorizationasynchronously(withtimeoutinterval:completionhandler:).md)
  Presents the user the opportunity to authorize the content for playback.
- [enum AVContentAuthorizationStatus](avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](avplayeritem/cancelcontentauthorizationrequest.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/contentauthorizationrequeststatus)*