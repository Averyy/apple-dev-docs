# requestAuthorization(completionHandler:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Asks the system for access to the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func requestAuthorization(completionHandler: (@Sendable (INFocusStatusAuthorizationStatus) -> Void)? = nil)
```

```swift
func requestAuthorization() async -> INFocusStatusAuthorizationStatus
```

```objc
- (void) requestAuthorizationWithCompletionHandler:(void (^)(INFocusStatusAuthorizationStatus status)) completionHandler;
```

## Discussion

Call this method from your app to request authorization to access the user’s focus status. The first time you make this request, the system prompts the user to grant or deny permission.

## Parameters

- `completionHandler`: The handler block to execute when the authorization status for your app is determined. This block has no return value and takes the following parameter:

  - **status**: The authorization status of your app. For a list of possible values, see [`INFocusStatusAuthorizationStatus`](../infocusstatusauthorizationstatus.md).

## See Also

### Requesting Authorization
- [var authorizationStatus: INFocusStatusAuthorizationStatus](./authorizationstatus.md)
  Returns your app’s current ability to access the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatuscenter/requestauthorization(completionhandler:))*