# init(_:including:)

**Framework**: Foundation  
**Kind**: init

Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.

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
convenience init<S>(_ attrStr: AttributedString, including scope: KeyPath<AttributeScopes, S.Type>) throws where S : AttributeScope
```

## Parameters

- `attrStr`: The value-type attributed string that provides the text and attributes of the new object.
- `scope`: A key path that identifies the attribute scope of the attributes in  . This can be a nested scope that contains several scopes.

## See Also

- [convenience init(AttributedString)](nsattributedstring/init(_:).md)
  Creates a reference-type attributed string from the specified value-type attributed string.
- [convenience init<S>(AttributedString, including: S.Type) throws](nsattributedstring/init(_:including:)-9gogq.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(_:including:)-8iy4i)*