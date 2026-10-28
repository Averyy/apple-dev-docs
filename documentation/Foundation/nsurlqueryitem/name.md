# name

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The name of the query item.

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
var name: String { get }
```

```objc
@property (readonly) NSString * name;
```

## Discussion

For example, in the URL `http://www.apple.com/search/?q=iPad`, the `name` parameter is `q`.

This string is not percent-encoded.

## See Also

### Related Documentation
- [var queryItems: [URLQueryItem]?](../nsurlcomponents/queryitems.md)
  The query URL component as an array of name/value pairs.
### Reading a Query Item’s Name and Value
- [var value: String?](./value.md)
  The value for the query item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlqueryitem/name)*