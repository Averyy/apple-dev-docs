# isApplicationAuthorizedForPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the application can be used to play the content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
var isApplicationAuthorizedForPlayback: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isApplicationAuthorizedForPlayback) BOOL applicationAuthorizedForPlayback;
```

#### Discussion

This property reports whether or not the calling application is authorized to play the content associated with the item.

Application authorization is independent of content authorization (see [`isContentAuthorizedForPlayback`](./iscontentauthorizedforplayback.md)) and that both must be granted in order for an application to be allowed to play protected content. Also, unlike content authorization, application authorization is not dependent on user credentials (that is, if `applicationAuthorizedForPlayback` is [`false`](../../Swift/false.md), there are no means to obtain authorization).

This property is not key-value observable.

## See Also

### Managing playback authorization in macOS
- [var isContentAuthorizedForPlayback: Bool](./iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isAuthorizationRequiredForPlayback: Bool](./isauthorizationrequiredforplayback.md)
  A Boolean value that indicates whether authorization is required to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](./requestcontentauthorizationasynchronously%28withtimeoutinterval,completionhandler%29.md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](./contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [enum AVContentAuthorizationStatus](../avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](./cancelcontentauthorizationrequest%28%29.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isapplicationauthorizedforplayback)*