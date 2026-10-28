# reportSpam(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method  
**Role**: Instance Method

Reports an RCS message as spam to the carrier and to partners.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final func reportSpam(_ request: RCSService.ReportSpamRequest) async throws
```

## Discussion

> **Throws**:  If the session is no longer valid, this method throws [`TelephonyMessagingSession.Error.invalidSession`](../telephonymessagingsession/error/invalidsession.md). If the carrier doesn’t support spam reporting, the method throws [`RCSService.Error.notSupported`](./error/notsupported.md).

## Parameters

- `request`: A request that provides details about the spam message.

## See Also

### Reporting spam
- [RCSService.ReportSpamRequest](./reportspamrequest.md)
  A structure that contains information about a spam reporting request for an RCS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspam(_:))*