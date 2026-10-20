# isAuthorizationRequiredForPlayback

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether authorization is required to play the content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
var isAuthorizationRequiredForPlayback: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAuthorizationRequiredForPlayback) BOOL authorizationRequiredForPlayback;
```

#### Discussion

This property reports whether authorization is required for the item’s content to be played. If it does not require authorization, then none of the other authorization-related  methods or properties apply (though they will return sensible values where possible).

This property is not key-value observable.

## See Also

### Managing playback authorization in macOS
- [var isContentAuthorizedForPlayback: Bool](./iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
- [var isApplicationAuthorizedForPlayback: Bool](./isapplicationauthorizedforplayback.md)
  A Boolean value that indicates whether the application can be used to play the content.
- [func requestContentAuthorizationAsynchronously(withTimeoutInterval: TimeInterval, completionHandler: () -> Void)](./requestcontentauthorizationasynchronously%28withtimeoutinterval,completionhandler%29.md)
  Presents the user the opportunity to authorize the content for playback.
- [var contentAuthorizationRequestStatus: AVContentAuthorizationStatus](./contentauthorizationrequeststatus.md)
  The status of the most recent content authorization request.
- [enum AVContentAuthorizationStatus](../avcontentauthorizationstatus.md)
  A value representing the status of a content authorization request.
- [func cancelContentAuthorizationRequest()](./cancelcontentauthorizationrequest%28%29.md)
  Cancels the currently outstanding content authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isauthorizationrequiredforplayback)*