# removeCookies(since:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes cookies that were stored after a given date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeCookies(since date: Date)
```

```objc
- (void) removeCookiesSinceDate:(NSDate *) date;
```

## Parameters

- `date`: The date after which cookies should be removed.

## See Also

### Adding and removing cookies
- [func deleteCookie(HTTPCookie)](./deletecookie%28_%29.md)
  Deletes the specified cookie from the cookie storage.
- [func setCookie(HTTPCookie)](./setcookie%28_%29.md)
  Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [func setCookies([HTTPCookie], for: URL?, mainDocumentURL: URL?)](./setcookies%28_,for,maindocumenturl%29.md)
  Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.
- [func storeCookies([HTTPCookie], for: URLSessionTask)](./storecookies%28_,for%29.md)
  Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/removecookies(since:))*