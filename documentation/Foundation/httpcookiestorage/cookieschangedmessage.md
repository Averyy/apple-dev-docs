# HTTPCookieStorage.CookiesChangedMessage

**Framework**: Foundation  
**Kind**: struct

A message a cookie storage instance sends when its cookies change.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct CookiesChangedMessage
```

#### Overview

Observe this message with the identifier [`cookiesChanged`](notificationcenter/messageidentifier/cookieschanged.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`HTTPCookieStorage`](httpcookiestorage.md).

This message interoperates with the notification [`NSHTTPCookieManagerCookiesChanged`](nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](httpcookiestorage/cookieschangedmessage/init.md)
  Creates a message that the cookies in a cookie storage instance changed.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md)
  A notification posted when the cookies stored in the cookie storage have changed.
- [static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged.md)
  A notification posted when the acceptance policy of the cookie storage has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/cookieschangedmessage)*