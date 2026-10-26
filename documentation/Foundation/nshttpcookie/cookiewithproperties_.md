# cookieWithProperties:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and initializes an HTTP cookie object using the provided properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSHTTPCookie *) cookieWithProperties:(NSDictionary<NSString *,id> *) properties;
```

#### Return Value

The newly created cookie object. Returns `nil` if the provided properties are invalid.

#### Discussion

To successfully create a cookie, you must provide values for (at least) the [`path`](../httpcookiepropertykey/path.md), [`name`](../httpcookiepropertykey/name.md), and [`value`](../httpcookiepropertykey/value.md) keys, and either the [`originURL`](../httpcookiepropertykey/originurl.md) key or the [`domain`](../httpcookiepropertykey/domain.md) key.

See Accepting cookies for more information on the available cookie attribute constants and the constraints imposed on the values in the dictionary.

## Parameters

- `properties`: The properties for the new cookie object, expressed as key value pairs.

## See Also

### Creating cookies
- [class func cookies(withResponseHeaderFields: [String : String], for: URL) -> [HTTPCookie]](../httpcookie/cookies%28withresponseheaderfields,for%29.md)
  Creates an array of HTTP cookies that corresponds to the provided response header fields for the provided URL.
- [init?(properties: [HTTPCookiePropertyKey : Any])](../httpcookie/init%28properties%29.md)
  Initializes an HTTP cookie object with the given cookie properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshttpcookie/cookiewithproperties:)*