# init(_:including:)

**Framework**: Foundation  
**Kind**: init

Creates a value-type attributed string from a reference type, including an attribute scope that a key path identifies.

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
init<S>(_ nsStr: NSAttributedString, including scope: KeyPath<AttributeScopes, S.Type>) throws where S : AttributeScope
```

#### Discussion

This initializer only collects attributes from `nsStr` that exist in the provided scope. The resulting attributed string omits any keys in `nsStr` that don’t exist in `scope`.

## Parameters

- `nsStr`: The   to convert.
- `scope`: A key path that identifies the attribute scope of the attributes in  . This can be a nested scope that contains several scopes.

## See Also

- [init<S>(NSAttributedString, including: S.Type) throws](attributedstring/init(_:including:)-9no47.md)
  Creates a value-type attributed string from a reference type, including an attribute scope.
- [init(NSAttributedString)](attributedstring/init(_:)-1fru0.md)
  Creates a value-type attributed string from a reference type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(_:including:)-puv0)*