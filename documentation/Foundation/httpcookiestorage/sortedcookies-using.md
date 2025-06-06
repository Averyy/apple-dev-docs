# sortedCookies(using:)

**Framework**: Foundation  
**Kind**: method

Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sortedCookies(using sortOrder: [NSSortDescriptor]) -> [HTTPCookie]
```

#### Return Value

The cookie storage’s cookies, sorted according to `sortOrder`, as an array of [`HTTPCookie`](httpcookie.md) objects.

## Parameters

- `sortOrder`: The sort descriptors to use for sorting, as an array of   objects.

## See Also

- [var cookies: [HTTPCookie]?](httpcookiestorage/cookies.md)
  The cookie storage’s cookies.
- [func getCookiesFor(URLSessionTask, completionHandler: ([HTTPCookie]?) -> Void)](httpcookiestorage/getcookiesfor(_:completionhandler:).md)
  Fetches cookies relevant to the specified task and passes them to the completion handler.
- [func cookies(for: URL) -> [HTTPCookie]?](httpcookiestorage/cookies(for:).md)
  Returns all the cookie storage’s cookies that are sent to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/sortedcookies(using:))*