# requestHeaderFields(with:)

**Framework**: Foundation  
**Kind**: method

Converts an array of cookies to a dictionary of header fields.

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
class func requestHeaderFields(with cookies: [HTTPCookie]) -> [String : String]
```

#### Return Value

The dictionary of header fields created from the provided cookies.

#### Discussion

To send these headers as part of a URL request to a remote server, create an [`NSMutableURLRequest`](nsmutableurlrequest.md) object, then call the [`allHTTPHeaderFields`](nsmutableurlrequest/allhttpheaderfields.md) or [`setValue(_:forHTTPHeaderField:)`](nsmutableurlrequest/setvalue(_:forhttpheaderfield:).md) method to set the provided headers for the request. Finally, initialize and start an [`URLSessionTask`](urlsessiontask.md) instance based on that request object.

## Parameters

- `cookies`: The cookies from which the header fields are created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/requestheaderfields(with:))*