# value(forHTTPHeaderField:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) valueForHTTPHeaderField:(NSString *) field;
```

## Return Value

The value associated with the header field `field`, or `nil` if there is no corresponding header field.

## Parameters

- `field`: The name of the header field whose value is to be returned. In keeping with the HTTP RFC, HTTP header field names are case-insensitive.

## See Also

### Related Documentation
- [func addValue(String, forHTTPHeaderField: String)](../nsmutableurlrequest/addvalue%28_,forhttpheaderfield%29.md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](../nsmutableurlrequest/setvalue%28_,forhttpheaderfield%29.md)
  Sets a value for the header field.
### Getting header fields
- [var allHTTPHeaderFields: [String : String]?](./allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/value(forhttpheaderfield:))*