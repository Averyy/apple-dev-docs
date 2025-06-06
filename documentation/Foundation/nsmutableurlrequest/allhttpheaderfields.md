# allHTTPHeaderFields

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

Certain header fields are reserved (see [`Reserved HTTP headers`](nsurlrequest#Reserved-HTTP-headers.md)). Do not use this property to set such headers.

## See Also

- [func addValue(String, forHTTPHeaderField: String)](nsmutableurlrequest/addvalue(_:forhttpheaderfield:).md)
  Adds a value to the header field.
- [func setValue(String?, forHTTPHeaderField: String)](nsmutableurlrequest/setvalue(_:forhttpheaderfield:).md)
  Sets a value for the header field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allhttpheaderfields)*