# setValue(_:forHTTPHeaderField:)

**Framework**: Foundation  
**Kind**: method

Sets a value for the header field.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func setValue(_ value: String?, forHTTPHeaderField field: String)
```

## Mentions

- [Uploading data to a website](uploading-data-to-a-website.md)

#### Discussion

Certain header fields are reserved. Do not use this method to set such headers. Specifically, there is no need for you to set the `Content-Length` header. See [`Reserved HTTP headers`](nsurlrequest#Reserved-HTTP-headers.md).

## Parameters

- `value`: The new value for the header field. Any existing value for the field is replaced by the new value.
- `field`: The name of the header field to set. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## See Also

- [var allHTTPHeaderFields: [String : String]?](urlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func addValue(String, forHTTPHeaderField: String)](urlrequest/addvalue(_:forhttpheaderfield:).md)
  Adds a value to the header field.
- [func value(forHTTPHeaderField: String) -> String?](urlrequest/value(forhttpheaderfield:).md)
  Retrieves a header value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/setvalue(_:forhttpheaderfield:))*