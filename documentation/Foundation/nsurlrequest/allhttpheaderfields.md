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
var allHTTPHeaderFields: [String : String]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<NSString *,NSString *> * allHTTPHeaderFields;
```

## See Also

### Related Documentation
- [var allHTTPHeaderFields: [String : String]?](../nsmutableurlrequest/allhttpheaderfields.md)
  A dictionary containing all of the HTTP header fields for a request.
### Getting header fields
- [func value(forHTTPHeaderField: String) -> String?](./value%28forhttpheaderfield%29.md)
  Returns the value of the specified HTTP header field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/allhttpheaderfields)*