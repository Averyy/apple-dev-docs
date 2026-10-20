# storeCookies(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Stores an array of cookies in the cookie storage, on behalf of the provided task, if the cookie accept policy permits.

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
func storeCookies(_ cookies: [HTTPCookie], for task: URLSessionTask)
```

```objc
- (void) storeCookies:(NSArray<NSHTTPCookie *> *) cookies forTask:(NSURLSessionTask *) task;
```

## Parameters

- `cookies`: The cookies to add.
- `task`: The task that handles the response. Override this method and inspect this parameter if you need to alter your cookie storage strategy based on properties of the task.

## See Also

### Adding and removing cookies
- [func removeCookies(since: Date)](./removecookies%28since%29.md)
  Removes cookies that were stored after a given date.
- [func deleteCookie(HTTPCookie)](./deletecookie%28_%29.md)
  Deletes the specified cookie from the cookie storage.
- [func setCookie(HTTPCookie)](./setcookie%28_%29.md)
  Stores a specified cookie in the cookie storage if the cookie accept policy permits.
- [func setCookies([HTTPCookie], for: URL?, mainDocumentURL: URL?)](./setcookies%28_,for,maindocumenturl%29.md)
  Adds an array of cookies to the cookie storage if the storage’s cookie acceptance policy permits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/storecookies(_:for:))*