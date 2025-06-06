# NSHTTPCookieManagerCookiesChanged

**Framework**: Foundation  
**Kind**: property

A notification posted when the cookies stored in the cookie storage have changed.

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
static let NSHTTPCookieManagerCookiesChanged: NSNotification.Name
```

#### Discussion

The notification’s [`object`](notification/object.md) is the [`HTTPCookieStorage`](httpcookiestorage.md) instance. This notification does not contain a [`userInfo`](notification/userinfo.md) dictionary.

## See Also

- [static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name](nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged.md)
  A notification posted when the acceptance policy of the cookie storage has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nshttpcookiemanagercookieschanged)*