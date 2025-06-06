# value(forHTTPHeaderField:)

**Framework**: Foundation  
**Kind**: method

Retrieves a header value.

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
func value(forHTTPHeaderField field: String) -> String?
```

#### Return Value

The value associated with the header field field,  or `nil` if there is no corresponding header field.

#### Discussion

Note that, in keeping with the HTTP RFC, HTTP header field names are case-insensitive.

## Parameters

- `field`: The header field name to use for the lookup (case-insensitive).

## See Also

- [var allHTTPHeaderFields: [String : String]?](urlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func addValue(String, forHTTPHeaderField: String)](urlrequest/addvalue(_:forhttpheaderfield:).md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](urlrequest/setvalue(_:forhttpheaderfield:).md)
  Sets a value for the header field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/value(forhttpheaderfield:))*