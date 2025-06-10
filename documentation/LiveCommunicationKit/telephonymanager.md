# TelephonyManager

**Framework**: LiveCommunicationKit  
**Kind**: class

An interface for initiating cellular network or VoIP conversations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
class TelephonyManager
```

## Mentions

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)
- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)

#### Overview

Use `TelephonyManager` to initiate a conversation and let the system route the conversation to the default calling app. For more information, see [`Preparing your app to be the default dialer app`](preparing-your-app-to-be-the-default-dialer-app.md).

## Topics

### Dialing
- [init()](telephonymanager/init.md)
  Creates a manager object for initiating conversations.
- [func dial(request: DialRequest) async throws](telephonymanager/dial(request:).md)
  Dials using the provided request to initiate a conversation.
### Accounts
- [var accounts: [Account]](telephonymanager/accounts.md)
  The list of accounts that an application can use to initiate a conversation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DialRequest](dialrequest.md)
  A request to start a conversation using the default calling app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/telephonymanager)*