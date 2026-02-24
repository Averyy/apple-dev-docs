# requestPlaybackRestrictionsAuthorization(_:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether this item is subject to parental restrictions, and, if so, prompts the user to enter the restrictions passcode.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func requestPlaybackRestrictionsAuthorization() async throws -> Bool
```

## Parameters

- `completion`: A callback the system invokes after it makes a determination of parental restrictions. - **`isAuthorized`**: A Boolean value that indicates whether the system authorizes the app to play an item.
- **`error`**: An optional error that contains error details if the system encountered an error.

## See Also

- [func cancelPlaybackRestrictionsAuthorizationRequest()](avplayeritem/cancelplaybackrestrictionsauthorizationrequest.md)
  Cancels a pending authorization request and dismisses the passcode entry, if displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/requestplaybackrestrictionsauthorization(_:))*