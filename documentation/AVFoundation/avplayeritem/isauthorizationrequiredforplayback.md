# isAuthorizationRequiredForPlayback

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether authorization is required to play the content.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
@MainActor
var isAuthorizationRequiredForPlayback: Bool { get }
```

#### Discussion

This property reports whether authorization is required for the item’s content to be played. If it does not require authorization, then none of the other authorization-related  methods or properties apply (though they will return sensible values where possible).

This property is not key-value observable.

## See Also

- [var isContentAuthorizedForPlayback: Bool](avplayeritem/iscontentauthorizedforplayback.md)
  A Boolean value that indicates whether the content has been authorized by the user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/isauthorizationrequiredforplayback)*