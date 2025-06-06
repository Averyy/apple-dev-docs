# cookies

**Framework**: Foundation  
**Kind**: property

The cookie storage’s cookies.

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
var cookies: [HTTPCookie]? { get }
```

#### Discussion

If you want to sort the cookie storage’s cookies, you should use the [`sortedCookies(using:)`](httpcookiestorage/sortedcookies(using:).md) method instead of sorting the result of this method.

## See Also

- [func getCookiesFor(URLSessionTask, completionHandler: ([HTTPCookie]?) -> Void)](httpcookiestorage/getcookiesfor(_:completionhandler:).md)
  Fetches cookies relevant to the specified task and passes them to the completion handler.
- [func cookies(for: URL) -> [HTTPCookie]?](httpcookiestorage/cookies(for:).md)
  Returns all the cookie storage’s cookies that are sent to a specified URL.
- [func sortedCookies(using: [NSSortDescriptor]) -> [HTTPCookie]](httpcookiestorage/sortedcookies(using:).md)
  Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/cookies)*