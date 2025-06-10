# sendDeviceSpecifics(to:using:messageID:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends device specifics in response to a suggested action to send device specifics.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func sendDeviceSpecifics(to destination: RCSHandle.URI, using cellularServiceID: CellularServiceID, messageID: RCSMessageID) async throws
```

#### Discussion

Call this method after the person using the app selects a [`RCSService.Business.Suggestion`](rcsservice/business/suggestion.md) of type [`RCSService.Business.Suggestion.action(_:)`](rcsservice/business/suggestion/action(_:).md), whose action type is [`RCSService.Business.SuggestedAction.Action.sendDeviceSpecifics`](rcsservice/business/suggestedaction/action-swift.enum/senddevicespecifics.md) .

> **Note**:  If the session is no longer valid, this method throws [`TelephonyMessagingSession.Error.invalidSession`](telephonymessagingsession/error/invalidsession.md). If the method can’t process the request for other reasons it throws [`RCSService.Error.internalError`](rcsservice/error/internalerror.md).

## Parameters

- `destination`: The destination handle to send device specifics to.
- `cellularServiceID`: The service identifier to use for the message.
- `messageID`: The message identifier to use for the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/senddevicespecifics(to:using:messageid:))*