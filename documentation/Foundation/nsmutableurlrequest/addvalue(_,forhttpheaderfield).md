# addValue(_:forHTTPHeaderField:)

**Framework**: Foundation  
**Kind**: method

Adds a value to the header field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addValue(_ value: String, forHTTPHeaderField field: String)
```

#### Discussion

This method provides the ability to add values to header fields incrementally. If a value was previously set for the specified field, the supplied value is appended to the existing value using the appropriate field delimiter (a comma).

Certain header fields are reserved (see [`Reserved HTTP headers`](nsurlrequest#Reserved-HTTP-headers.md)). Do not use this method to change such headers.

## Parameters

- `value`: The value for the header field.
- `field`: The name of the header field. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## See Also

- [func value(forHTTPHeaderField: String) -> String?](nsurlrequest/value(forhttpheaderfield:).md)
  Returns the value of the specified HTTP header field.
- [var allHTTPHeaderFields: [String : String]?](nsmutableurlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func setValue(String?, forHTTPHeaderField: String)](nsmutableurlrequest/setvalue(_:forhttpheaderfield:).md)
  Sets a value for the header field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/addvalue(_:forhttpheaderfield:))*