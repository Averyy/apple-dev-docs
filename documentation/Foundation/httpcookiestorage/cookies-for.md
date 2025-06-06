# cookies(for:)

**Framework**: Foundation  
**Kind**: method

Returns all the cookie storage’s cookies that are sent to a specified URL.

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
func cookies(for URL: URL) -> [HTTPCookie]?
```

#### Return Value

An array of cookies whose URL matches the provided URL.

#### Discussion

You can use the [`requestHeaderFields(with:)`](httpcookie/requestheaderfields(with:).md) method of [`HTTPCookie`](httpcookie.md) to turn the array returned by this method into a set of header fields to add to a [`URLRequest`](urlrequest.md) object (or [`NSMutableURLRequest`](nsmutableurlrequest.md) in Objective-C).

If you override this method, also override [`getCookiesFor(_:completionHandler:)`](httpcookiestorage/getcookiesfor(_:completionhandler:).md).

## Parameters

- `URL`: The URL to filter on.

## See Also

- [var cookies: [HTTPCookie]?](httpcookiestorage/cookies.md)
  The cookie storage’s cookies.
- [func getCookiesFor(URLSessionTask, completionHandler: ([HTTPCookie]?) -> Void)](httpcookiestorage/getcookiesfor(_:completionhandler:).md)
  Fetches cookies relevant to the specified task and passes them to the completion handler.
- [func sortedCookies(using: [NSSortDescriptor]) -> [HTTPCookie]](httpcookiestorage/sortedcookies(using:).md)
  Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/cookies(for:))*