# consumeOneTimeCode(_:)

**Framework**: Authentication Services  
**Kind**: method

Mark a one-time code as “consumed” by the current process.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func consumeOneTimeCode(_ oneTimeCode: ASVerificationCode) async throws
```

#### Discussion

A code should only be marked as consumed if it was submitted to a service for the purposes of authentication.

Consuming a code will mark a code’s containing message as read in the Messages and Mail apps. Depending on the user’s preference, this may also delete the code’s containing message.

> **Note**: `ASDeliveredVerificationCodesManager.VerificationError` if the system failed to accept the update.

> **Note**: Only consume codes that you submit to a service. You should make a best effort to ensure it is accepted before calling this.

## Parameters

- `oneTimeCode`: The code to mark as consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asdeliveredverificationcodesmanager/consumeonetimecode(_:))*