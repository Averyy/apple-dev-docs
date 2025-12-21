# reportSpam(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Reports an SMS message as spam to the carrier and to partners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func reportSpam(_ message: SMSMessage) async throws
```

#### Discussion

> **Note**:  A [`TelephonyMessagingSession.Error.invalidSession`](telephonymessagingsession/error/invalidsession.md) if the session is no longer valid or an [`SMSService.Error.notSupported`](smsservice/error/notsupported.md) if the carrier doesn’t support spam reporting.

## Parameters

- `message`:   to report as spam.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/reportspam(_:))*