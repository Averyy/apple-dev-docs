# setCookie(_:)

**Framework**: Foundation  
**Kind**: method

Stores a specified cookie in the cookie storage if the cookie accept policy permits.

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
func setCookie(_ cookie: HTTPCookie)
```

#### Discussion

The cookie replaces an existing cookie with the same name, domain, and path, if one exists in the cookie storage. This method accepts the cookie only if the storage’s cookie accept policy is [`HTTPCookie.AcceptPolicy.always`](httpcookie/acceptpolicy/always.md) or [`HTTPCookie.AcceptPolicy.onlyFromMainDocumentDomain`](httpcookie/acceptpolicy/onlyfrommaindocumentdomain.md). The cookie is ignored if the storage’s cookie accept policy is [`HTTPCookie.AcceptPolicy.never`](httpcookie/acceptpolicy/never.md).

## Parameters

- `cookie`: The cookie to store.

## See Also

- [func removeCookies(since: Date)](httpcookiestorage/removecookies(since:).md)
  Removes cookies that were stored after a given date.
- [func deleteCookie(HTTPCookie)](httpcookiestorage/deletecookie(_:).md)
  Deletes the specified cookie from the cookie storage.
- [func setCookies([HTTPCookie], for: URL?, mainDocumentURL: URL?)](httpcookiestorage/setcookies(_:for:maindocumenturl:).md)
  Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [func storeCookies([HTTPCookie], for: URLSessionTask)](httpcookiestorage/storecookies(_:for:).md)
  Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/setcookie(_:))*