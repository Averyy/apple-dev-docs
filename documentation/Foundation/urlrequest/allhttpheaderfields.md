# allHTTPHeaderFields

**Framework**: Foundation  
**Kind**: property

A dictionary containing all of the HTTP header fields for a request.

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
var allHTTPHeaderFields: [String : String]? { get set }
```

#### Discussion

Certain header fields are reserved (see [`Reserved HTTP headers`](nsurlrequest#Reserved-HTTP-headers.md)). Do not use this property to set such headers.

## See Also

- [func addValue(String, forHTTPHeaderField: String)](urlrequest/addvalue(_:forhttpheaderfield:).md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](urlrequest/setvalue(_:forhttpheaderfield:).md)
  Sets a value for the header field.
- [func value(forHTTPHeaderField: String) -> String?](urlrequest/value(forhttpheaderfield:).md)
  Retrieves a header value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlrequest/allhttpheaderfields)*