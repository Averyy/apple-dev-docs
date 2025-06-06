# deleteCookie(_:)

**Framework**: Foundation  
**Kind**: method

Deletes the specified cookie from the cookie storage.

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
func deleteCookie(_ cookie: HTTPCookie)
```

## Parameters

- `cookie`: The cookie to delete.

## See Also

- [func removeCookies(since: Date)](httpcookiestorage/removecookies(since:).md)
  Removes cookies that were stored after a given date.
- [func setCookie(HTTPCookie)](httpcookiestorage/setcookie(_:).md)
  Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [func setCookies([HTTPCookie], for: URL?, mainDocumentURL: URL?)](httpcookiestorage/setcookies(_:for:maindocumenturl:).md)
  Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [func storeCookies([HTTPCookie], for: URLSessionTask)](httpcookiestorage/storecookies(_:for:).md)
  Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/deletecookie(_:))*