# cookieAcceptPolicy

**Framework**: Foundation  
**Kind**: property

The cookie storage’s cookie accept policy.

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
var cookieAcceptPolicy: HTTPCookie.AcceptPolicy { get set }
```

#### Discussion

The default cookie accept policy is [`HTTPCookie.AcceptPolicy.always`](httpcookie/acceptpolicy/always.md). Changing the cookie policy affects all currently running applications using the cookie storage.

## See Also

- [HTTPCookie.AcceptPolicy](httpcookie/acceptpolicy.md)
  Cookie acceptance policies implemented by the [`HTTPCookieStorage`](httpcookiestorage.md) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/cookieacceptpolicy)*