# setCookies(_:for:mainDocumentURL:)

**Framework**: Foundation  
**Kind**: method

Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.

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
func setCookies(_ cookies: [HTTPCookie], for URL: URL?, mainDocumentURL: URL?)
```

#### Discussion

Cookies in the array will replace existing cookies with the same name, domain, and path in the cookie storage. If the storage has an accept policy of [`HTTPCookie.AcceptPolicy.never`](httpcookie/acceptpolicy/never.md), the cookies are ignored.

To store cookies from a set of response headers, an application can use [`cookies(withResponseHeaderFields:for:)`](httpcookie/cookies(withresponseheaderfields:for:).md) passing a header field dictionary and then use this method to store the resulting cookies in accordance with the cookie storage’s cookie acceptance policy.

If you override this method, also override [`storeCookies(_:for:)`](httpcookiestorage/storecookies(_:for:).md).

## Parameters

- `cookies`: The cookies to add.
- `URL`: The URL associated with the added cookies.
- `mainDocumentURL`: The URL of the main HTML document for the top-level frame, if known. The value can be  . This URL is used to determine whether the cookie should be accepted if the cookie accept policy is  .

## See Also

- [func removeCookies(since: Date)](httpcookiestorage/removecookies(since:).md)
  Removes cookies that were stored after a given date.
- [func deleteCookie(HTTPCookie)](httpcookiestorage/deletecookie(_:).md)
  Deletes the specified cookie from the cookie storage.
- [func setCookie(HTTPCookie)](httpcookiestorage/setcookie(_:).md)
  Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [func storeCookies([HTTPCookie], for: URLSessionTask)](httpcookiestorage/storecookies(_:for:).md)
  Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/setcookies(_:for:maindocumenturl:))*