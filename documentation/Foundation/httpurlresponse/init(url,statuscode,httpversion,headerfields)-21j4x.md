# init(url:statusCode:httpVersion:headerFields:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an HTTP URL response object with a status code, protocol version, and response headers.

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
init?(url: URL, statusCode: Int, httpVersion HTTPVersion: String?, headerFields: [String : String]?)
```

```objc
- (instancetype) initWithURL:(NSURL *) url statusCode:(NSInteger) statusCode HTTPVersion:(NSString *) HTTPVersion headerFields:(NSDictionary<NSString *,NSString *> *) headerFields;
```

#### Return Value

An initialized [`HTTPURLResponse`](../httpurlresponse.md) object or `nil` if an error occurred during initialization.

## Parameters

- `url`: The URL from which the response was generated.
- `statusCode`: The HTTP status code to return (`404`, for example). See [RFC 2616](http://www.ietf.org/rfc/rfc2616.txt) for details.
- `HTTPVersion`: The version of the HTTP response as returned by the server. This is typically represented as “HTTP/1.1”.
- `headerFields`: A dictionary representing the keys and values from the server’s response header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpurlresponse/init(url:statuscode:httpversion:headerfields:)-21j4x)*