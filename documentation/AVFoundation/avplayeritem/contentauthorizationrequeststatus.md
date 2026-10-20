# contentAuthorizationRequestStatus

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The status of the most recent content authorization request.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var contentAuthorizationRequestStatus: AVContentAuthorizationStatus { get }
```

```objc
@property (nonatomic, readonly) AVContentAuthorizationStatus contentAuthorizationRequestStatus;
```

#### Discussion

This property reports the authorization status as determined by the most recent call to [`requestContentAuthorizationAsynchronously(withTimeoutInterval:completionHandler:)`](./requestcontentauthorizationasynchronously%28withtimeoutinterval,completionhandler%29.md).

The value will be [`AVContentAuthorizationStatus.unknown`](../avcontentauthorizationstatus/unknown.md) before the first call and between the time a request call is made and just prior to the completion handler being executed (thus it is safe to query this property from the completion handler).

This value is not key-value observable.

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
- [enum AVContentAuthorizationStatus](../avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](./cancelcontentauthorizationrequest%28%29.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/contentauthorizationrequeststatus)*