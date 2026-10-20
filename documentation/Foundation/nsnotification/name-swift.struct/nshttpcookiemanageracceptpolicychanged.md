# NSHTTPCookieManagerAcceptPolicyChanged

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification posted when the acceptance policy of the cookie storage has changed.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.11
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Notification is never posted

## Declaration

```swift
static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name
```

```c
extern NSNotificationName const NSHTTPCookieManagerAcceptPolicyChangedNotification;
```

#### Discussion

In macOS, cookies are shared among applications, meaning this notification can be received as a result of another application’s actions. Cookies are not shared among applications in iOS.

The notification’s [`object`](../../notification/object.md) is the [`HTTPCookieStorage`](../../httpcookiestorage.md) instance. This notification does not contain a [`userInfo`](../../notification/userinfo.md) dictionary.

## See Also

### Tracking cookie storage changes
- [static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name](./nshttpcookiemanagercookieschanged.md)
  A notification posted when the cookies stored in the cookie storage have changed.
- [HTTPCookieStorage.CookiesChangedMessage](../../httpcookiestorage/cookieschangedmessage.md)
  A message a cookie storage instance sends when its cookies change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged)*