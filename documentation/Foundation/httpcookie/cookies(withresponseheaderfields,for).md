# cookies(withResponseHeaderFields:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an array of HTTP cookies that corresponds to the provided response header fields for the provided URL.

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
class func cookies(withResponseHeaderFields headerFields: [String : String], for URL: URL) -> [HTTPCookie]
```

```objc
+ (NSArray<NSHTTPCookie *> *) cookiesWithResponseHeaderFields:(NSDictionary<NSString *,NSString *> *) headerFields forURL:(NSURL *) URL;
```

#### Return Value

The array of created cookies.

#### Discussion

This method ignores irrelevant header fields in `headerFields`, allowing dictionaries to contain additional data.

If `headerFields` doesn’t specify a domain for a given cookie, the cookie is created with a default domain value of `URL`.

If `headerFields` doesn’t specify a path for a given cookie, the cookie is created with a default path value of `"/"`.

## Parameters

- `headerFields`: The header fields used to create the [`HTTPCookie`](../httpcookie.md) objects.
- `URL`: The URL associated with the created cookies.

## See Also

### Creating cookies
- [init?(properties: [HTTPCookiePropertyKey : Any])](./init%28properties%29.md)
  Initializes an HTTP cookie object with the given cookie properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/cookies(withresponseheaderfields:for:))*