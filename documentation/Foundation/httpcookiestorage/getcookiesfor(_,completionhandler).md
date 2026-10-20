# getCookiesFor(_:completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Fetches cookies relevant to the specified task and passes them to the completion handler.

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
func getCookiesFor(_ task: URLSessionTask, completionHandler: @escaping @Sendable ([HTTPCookie]?) -> Void)
```

```swift
func cookies(for task: URLSessionTask) async -> [HTTPCookie]?
```

```objc
- (void) getCookiesForTask:(NSURLSessionTask *) task completionHandler:(void (^)(NSArray<NSHTTPCookie *> *cookies)) completionHandler;
```

## Parameters

- `task`: The task performing a request. The cookie storage can use the URL and other properties of this task’s request to determine which cookies to fetch.
- `completionHandler`: A completion handler that receives an array of cookies as its argument.

## See Also

### Retrieving cookies
- [var cookies: [HTTPCookie]?](./cookies.md)
  The cookie storage’s cookies.
- [func cookies(for: URL) -> [HTTPCookie]?](./cookies%28for%29.md)
  Returns all the cookie storage’s cookies that are sent to a specified URL.
- [func sortedCookies(using: [NSSortDescriptor]) -> [HTTPCookie]](./sortedcookies%28using%29.md)
  Returns all of the cookie storage’s cookies, sorted according to a given set of sort descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/getcookiesfor(_:completionhandler:))*