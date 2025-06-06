# NSHTTPCookieManagerAcceptPolicyChanged

**Framework**: Foundation  
**Kind**: property

A notification posted when the acceptance policy of the cookie storage has changed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name
```

#### Discussion

In macOS, cookies are shared among applications, meaning this notification can be received as a result of another application’s actions. Cookies are not shared among applications in iOS.

The notification’s [`object`](notification/object.md) is the [`HTTPCookieStorage`](httpcookiestorage.md) instance. This notification does not contain a [`userInfo`](notification/userinfo.md) dictionary.

## See Also

- [static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged.md)
  A notification posted when the cookies stored in the cookie storage have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged)*