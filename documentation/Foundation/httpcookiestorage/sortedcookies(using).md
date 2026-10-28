# sortedCookies(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<NSHTTPCookie *> *) sortedCookiesUsingDescriptors:(NSArray<NSSortDescriptor *> *) sortOrder;
```

## Return Value

The cookie storage’s cookies, sorted according to `sortOrder`, as an array of [`HTTPCookie`](../httpcookie.md) objects.

## Parameters

- `sortOrder`: The sort descriptors to use for sorting, as an array of [`NSSortDescriptor`](../nssortdescriptor.md) objects.

## See Also

### Retrieving cookies
- [var cookies: [HTTPCookie]?](./cookies.md)
  The cookie storage’s cookies.
- [func getCookiesFor(URLSessionTask, completionHandler: ([HTTPCookie]?) -> Void)](./getcookiesfor%28_,completionhandler%29.md)
  Fetches cookies relevant to the specified task and passes them to the completion handler.
- [func cookies(for: URL) -> [HTTPCookie]?](./cookies%28for%29.md)
  Returns all the cookie storage’s cookies that are sent to a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookiestorage/sortedcookies(using:))*