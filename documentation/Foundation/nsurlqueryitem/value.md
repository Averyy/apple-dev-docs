# value

**Framework**: Foundation  
**Kind**: property

The value for the query item.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var value: String? { get }
```

#### Discussion

For example, in the URL `http://www.apple.com/search/?q=iPad`, the `value` parameter is `iPad`.

This string is not percent-encoded.

## See Also

- [var queryItems: [URLQueryItem]?](nsurlcomponents/queryitems.md)
  The query URL component as an array of name/value pairs.
- [var name: String](nsurlqueryitem/name.md)
  The name of the query item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlqueryitem/value)*