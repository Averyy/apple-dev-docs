# allHTTPHeaderFields

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A dictionary containing all of the HTTP header fields for a request.

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
var allHTTPHeaderFields: [String : String]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,NSString *> * allHTTPHeaderFields;
```

## Discussion

Certain header fields are reserved (see [Reserved HTTP headers](../nsurlrequest.md#Reserved-HTTP-headers)). Do not use this property to set such headers.

## See Also

### Accessing header fields
- [func addValue(String, forHTTPHeaderField: String)](./addvalue%28_,forhttpheaderfield%29.md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](./setvalue%28_,forhttpheaderfield%29.md)
  Sets a value for the header field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allhttpheaderfields)*