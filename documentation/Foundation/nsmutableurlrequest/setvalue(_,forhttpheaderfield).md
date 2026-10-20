# setValue(_:forHTTPHeaderField:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets a value for the header field.

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
func setValue(_ value: String?, forHTTPHeaderField field: String)
```

```objc
- (void) setValue:(NSString *) value forHTTPHeaderField:(NSString *) field;
```

#### Discussion

Certain header fields are reserved. Do not use this method to set such headers. Specifically, there is no need for you to set the `Content-Length` header. See [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers).

## Parameters

- `value`: The new value for the header field. Any existing value for the field is replaced by the new value.
- `field`: The name of the header field to set. In keeping with the HTTP RFC, HTTP header field names are case insensitive.

## See Also

### Related Documentation
- [func value(forHTTPHeaderField: String) -> String?](../nsurlrequest/value%28forhttpheaderfield%29.md)
  Returns the value of the specified HTTP header field.
### Accessing header fields
- [var allHTTPHeaderFields: [String : String]?](./allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
- [func addValue(String, forHTTPHeaderField: String)](./addvalue%28_,forhttpheaderfield%29.md)
  Adds a value to the header field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/setvalue(_:forhttpheaderfield:))*