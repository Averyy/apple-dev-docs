# oneTimeCodes(preferredDuration:anchor:)

**Framework**: Authentication Services  
**Kind**: method

Stream one-time codes received by the system.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func oneTimeCodes(preferredDuration: TimeInterval = 600, anchor: ASPresentationAnchor) async throws -> some AsyncSequence<ASVerificationCode, any Error>
```

#### Discussion

When requested, the user may decide whether your app may receive one-time codes. This stream will automatically disconnect after a period of time.

> **Note**: `ASDeliveredVerificationCodesManager.VerificationError` if one-time codes can not be delivered.

> **Note**: Only enabled credential providers may call this method.

## Parameters

- `preferredDuration`: How long the stream should ideally remain connected. This duration is not guaranteed and defaults to 10 minutes.
- `anchor`: The anchor for which any UI should be presented from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asdeliveredverificationcodesmanager/onetimecodes(preferredduration:anchor:)-tyrg)*