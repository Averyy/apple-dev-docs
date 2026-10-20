# cancelPlaybackRestrictionsAuthorizationRequest()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels a pending authorization request and dismisses the passcode entry, if displayed.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func cancelPlaybackRestrictionsAuthorizationRequest()
```

```objc
- (void) cancelPlaybackRestrictionsAuthorizationRequest;
```

## See Also

### Requesting playback authorization in tvOS
- [func requestPlaybackRestrictionsAuthorization((Bool, (any Error)?) -> Void)](./requestplaybackrestrictionsauthorization%28_%29.md)
  Determines whether this item is subject to parental restrictions, and, if so, prompts the user to enter the restrictions passcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/cancelplaybackrestrictionsauthorizationrequest())*