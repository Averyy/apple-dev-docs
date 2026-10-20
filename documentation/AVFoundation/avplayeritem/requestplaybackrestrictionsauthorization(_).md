# requestPlaybackRestrictionsAuthorization(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Determines whether this item is subject to parental restrictions, and, if so, prompts the user to enter the restrictions passcode.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func requestPlaybackRestrictionsAuthorization(_ completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func requestPlaybackRestrictionsAuthorization() async throws -> Bool
```

```objc
- (void) requestPlaybackRestrictionsAuthorization:(void (^)(BOOL isAuthorized, NSError *error)) completion;
```

## Parameters

- `completion`: A callback the system invokes after it makes a determination of parental restrictions.

  - **`isAuthorized`**: A Boolean value that indicates whether the system authorizes the app to play an item.
  - **`error`**: An optional error that contains error details if the system encountered an error.

## See Also

### Requesting playback authorization in tvOS
- [func cancelPlaybackRestrictionsAuthorizationRequest()](./cancelplaybackrestrictionsauthorizationrequest%28%29.md)
  Cancels a pending authorization request and dismisses the passcode entry, if displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/requestplaybackrestrictionsauthorization(_:))*