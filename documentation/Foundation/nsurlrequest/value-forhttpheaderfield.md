# value(forHTTPHeaderField:)

**Framework**: Foundation  
**Kind**: method

Returns the value of the specified HTTP header field.

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
func value(forHTTPHeaderField field: String) -> String?
```

#### Return Value

The value associated with the header field `field`, or `nil` if there is no corresponding header field.

## Parameters

- `field`: The name of the header field whose value is to be returned. In keeping with the HTTP RFC, HTTP header field names are case-insensitive.

## See Also

- [func addValue(String, forHTTPHeaderField: String)](nsmutableurlrequest/addvalue(_:forhttpheaderfield:).md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](nsmutableurlrequest/setvalue(_:forhttpheaderfield:).md)
  Sets a value for the header field.
- [var allHTTPHeaderFields: [String : String]?](nsurlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/value(forhttpheaderfield:))*