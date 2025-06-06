# init(_:including:)

**Framework**: Foundation  
**Kind**: init

Creates an attribute container from a dictionary and an attribute scope.

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
init<S>(_ dictionary: [NSAttributedString.Key : Any], including scope: S.Type) throws where S : AttributeScope
```

#### Discussion

This initializer only collects attributes from `dictionary` that exist in the provided scope. The resulting attribute container omits any keys in `dictionary` that don’t exist in `scope`.

## Parameters

- `dictionary`: A dictionary of attribute keys and their values.
- `scope`: The attribute scope of the dictionary keys. This can be a nested scope that contains several scopes.

## See Also

- [init()](attributecontainer/init.md)
  Creates an empty attribute container.
- [init<S>([NSAttributedString.Key : Any], including: KeyPath<AttributeScopes, S.Type>) throws](attributecontainer/init(_:including:)-28n0g.md)
  Creates an attribute container from a dictionary and an attribute scope that a key path identifies.
- [init([NSAttributedString.Key : Any])](attributecontainer/init(_:).md)
  Creates an attribute container from a dictionary, using default attribute scopes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/init(_:including:)-2mw0o)*