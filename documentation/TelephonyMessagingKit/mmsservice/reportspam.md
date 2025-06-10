# reportSpam(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Reports an MMS message as spam to the carrier and to partners.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func reportSpam(_ message: MMSMessage) async throws
```

#### Discussion

> **Note**: - `TelephonyMessagingSession.SessionError.invalidSession` when session has been invalidated.
- `MMSService.Error.notSupported` when spam reporting is not supported by carrier.

## Parameters

- `message`:   that needs to be reported as spam.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/reportspam(_:))*