# URLQueryItem

**Framework**: Foundation  
**Kind**: struct

A single name-value pair from the query portion of a URL.

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
struct URLQueryItem
```

## Topics

### Creating Query Items
- [init(name: String, value: String?)](urlqueryitem/init(name:value:).md)
  Creates a new query item with the name and value you specify.
### Accessing the Item’s Components
- [var name: String](urlqueryitem/name.md)
  The name of the query item.
- [var value: String?](urlqueryitem/value.md)
  The value for the query item.
### Using Reference Types
- [class NSURLQueryItem](nsurlqueryitem.md)
  An object representing a single name/value pair for an item in the query portion of a URL.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct URL](url.md)
  A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.
- [struct URLComponents](urlcomponents.md)
  A structure that parses URLs into and constructs URLs from their constituent parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlqueryitem)*