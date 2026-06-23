# CustomerEngagementSession.Error

**Framework**: ProximityReader  
**Kind**: enum

Errors that can occur during the engagement session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [CustomerEngagementSession.Error.connectionFailed](customerengagementsession/error/connectionfailed.md)
  An error occurred while connecting to the customer.
- [CustomerEngagementSession.Error.expiredCredential](customerengagementsession/error/expiredcredential.md)
  The credential used to create the session has expired.
- [CustomerEngagementSession.Error.incompatibleRequest](customerengagementsession/error/incompatiblerequest.md)
  An error that indicates the request is not compatible with the connected client type or version.
- [CustomerEngagementSession.Error.internalError](customerengagementsession/error/internalerror.md)
  An error that occurs internally within the session.
- [CustomerEngagementSession.Error.invalidCredential](customerengagementsession/error/invalidcredential.md)
  The credential used to create the session is not valid.
- [CustomerEngagementSession.Error.invalidPassTypeIdentifier](customerengagementsession/error/invalidpasstypeidentifier.md)
  An error that indicates the passTypeIdentifier validation failed.
- [CustomerEngagementSession.Error.invalidRequest](customerengagementsession/error/invalidrequest.md)
  An error that indicates the request validation failed.
- [CustomerEngagementSession.Error.invalidSession](customerengagementsession/error/invalidsession.md)
  The session is no longer active or is invalidated.
- [CustomerEngagementSession.Error.networkError](customerengagementsession/error/networkerror.md)
  This error can occur if the system can’t reach a necessary server. Your app needs to ask the user to check their network settings and allow them to try again.
- [CustomerEngagementSession.Error.notReady](customerengagementsession/error/notready.md)
  The session has not yet received the `.ready` event from the customer. The merchant must wait for the `.ready` event before sending requests.
- [CustomerEngagementSession.Error.notSupported](customerengagementsession/error/notsupported.md)
  The current device or the environment doesn’t support this feature.
- [CustomerEngagementSession.Error.pairingFailed](customerengagementsession/error/pairingfailed.md)
  An error occurred while pairing with the peer.
- [CustomerEngagementSession.Error.paymentRequestCancelled](customerengagementsession/error/paymentrequestcancelled.md)
  An error indicating the payment request to the customer was cancelled.
- [CustomerEngagementSession.Error.paymentRequestFailed](customerengagementsession/error/paymentrequestfailed.md)
  An error indicating the payment request to the customer failed.
- [CustomerEngagementSession.Error.requestCancelled](customerengagementsession/error/requestcancelled.md)
  An error indicating the request is cancelled.
- [CustomerEngagementSession.Error.requestFailed](customerengagementsession/error/requestfailed.md)
  An error that occurs while sending the request to the customer.
- [CustomerEngagementSession.Error.sessionBusy](customerengagementsession/error/sessionbusy.md)
  An error indicating the session is busy due to a pending request.
- [CustomerEngagementSession.Error.sessionFailed](customerengagementsession/error/sessionfailed.md)
  An error indicating that the framework failed to create the session.
- [CustomerEngagementSession.Error.userDeclined](customerengagementsession/error/userdeclined.md)
  An error indicating that the customer declined to share requested information.
- [CustomerEngagementSession.Error.wifiDisabled](customerengagementsession/error/wifidisabled.md)
  An error indicating that Wi-Fi is turned off.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/error)*