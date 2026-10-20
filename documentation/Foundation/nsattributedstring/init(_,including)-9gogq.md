# init(_:including:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init<S>(_ attrStr: AttributedString, including scope: S.Type) throws where S : AttributeScope
```

## Parameters

- `attrStr`: The value-type attributed string that provides the text and attributes of the new object.
- `scope`: The attribute scope of the attributes in `attrStr`. This can be a nested scope that contains several scopes.

## See Also

### Creating a formatted string
- [convenience init(AttributedString)](./init%28_%29.md)
  Creates a reference-type attributed string from the specified value-type attributed string.
- [convenience init<S>(AttributedString, including: KeyPath<AttributeScopes, S.Type>) throws](./init%28_,including%29-8iy4i.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(_:including:)-9gogq)*