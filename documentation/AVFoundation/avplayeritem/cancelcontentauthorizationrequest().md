# cancelContentAuthorizationRequest()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels the currently outstanding content authorization request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func cancelContentAuthorizationRequest()
```

```objc
- (void) cancelContentAuthorizationRequest;
```

## Discussion

Calling this method while a content authorization request is pending will cause that request to be cancelled and its completion handler to be invoked with a status of [`AVContentAuthorizationStatus.cancelled`](../avcontentauthorizationstatus/cancelled.md).

This method does not block.

## See Also

### Managing playback authorization in macOS
- [var isContentAuthorizedForPlayback: Bool](./iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](./isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [var isApplicationAuthorizedForPlayback: Bool](./isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](./requestcontentauthorizationasynchronously%28withtimeoutinterval,completionhandler%29.md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](./contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [enum AVContentAuthorizationStatus](../avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/cancelcontentauthorizationrequest())*