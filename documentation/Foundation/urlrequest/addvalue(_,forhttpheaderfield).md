# addValue(_:forHTTPHeaderField:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a value to the header field.

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
mutating func addValue(_ value: String, forHTTPHeaderField field: String)
```

## Discussion

This method provides the ability to add values to header fields incrementally. If a value was previously set for the specified field, the supplied value is appended to the existing value using the appropriate field delimiter (a comma).

Certain header fields are reserved (see [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers)). Do not use this method to change such headers.

## Parameters

- `value`: The value for the header field.
- `field`: The name of the header field. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## See Also

### Accessing header fields
- [var allHTTPHeaderFields: [String : String]?](./allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func setValue(String?, forHTTPHeaderField: String)](./setvalue%28_,forhttpheaderfield%29.md)
  Sets a value for the header field.
- [func value(forHTTPHeaderField: String) -> String?](./value%28forhttpheaderfield%29.md)
  Retrieves a header value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/addvalue(_:forhttpheaderfield:))*