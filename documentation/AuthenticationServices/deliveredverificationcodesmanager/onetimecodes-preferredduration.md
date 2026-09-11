# oneTimeCodes(preferredDuration:)

**Framework**: Authentication Services  
**Kind**: method

Stream one-time codes received by the system.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
func oneTimeCodes(preferredDuration: TimeInterval) async throws -> some AsyncSequence<ASVerificationCode, any Error>
```

#### Discussion

When requested, the user may decide whether your app may receive one-time codes. This stream will automatically disconnect after a period of time.

> **Note**: `DeliveredVerificationCodesManager.VerificationError` if one-time codes can not be delivered.

> **Note**: Only enabled credential providers may call this method.

## Parameters

- `preferredDuration`: How long the stream should ideally remain connected. This duration is not guaranteed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/deliveredverificationcodesmanager/onetimecodes(preferredduration:))*