# init(url:statusCode:httpVersion:headerFields:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

An initialized [`HTTPURLResponse`](httpurlresponse.md) object or `nil` if an error occurred during initialization.

## Parameters

- `url`: The URL from which the response was generated.
- `statusCode`: The HTTP status code to return ( , for example). See   for details.
- `HTTPVersion`: The version of the HTTP response as returned by the server. This is typically represented as “HTTP/1.1”.
- `headerFields`: A dictionary representing the keys and values from the server’s response header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpurlresponse/init(url:statuscode:httpversion:headerfields:))*