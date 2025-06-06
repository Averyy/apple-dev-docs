# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates an attribute container from a dictionary, using default attribute scopes.

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
init(_ dictionary: [NSAttributedString.Key : Any])
```

#### Discussion

This initializer includes all attribute scopes defined by the SDK, such as [`AttributeScopes.FoundationAttributes`](attributescopes/foundationattributes.md), [`AttributeScopes.SwiftUIAttributes`](attributescopes/swiftuiattributes.md), and [`AttributeScopes.AccessibilityAttributes`](attributescopes/accessibilityattributes.md). To use third-party attribute scopes, use the initializers [`init(_:including:)`](attributecontainer/init(_:including:)-2mw0o.md) and [`init(_:including:)`](attributecontainer/init(_:including:)-28n0g.md).

## Parameters

- `dictionary`: A dictionary of attribute keys and their values.

## See Also

- [init()](attributecontainer/init.md)
  Creates an empty attribute container.
- [init<S>([NSAttributedString.Key : Any], including: S.Type) throws](attributecontainer/init(_:including:)-2mw0o.md)
  Creates an attribute container from a dictionary and an attribute scope.
- [init<S>([NSAttributedString.Key : Any], including: KeyPath<AttributeScopes, S.Type>) throws](attributecontainer/init(_:including:)-28n0g.md)
  Creates an attribute container from a dictionary and an attribute scope that a key path identifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/init(_:))*