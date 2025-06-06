# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates a value-type attributed string from a reference type.

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
init(_ nsStr: NSAttributedString)
```

#### Discussion

This initializer includes all attribute scopes defined by the SDK, such as [`AttributeScopes.FoundationAttributes`](attributescopes/foundationattributes.md), [`AttributeScopes.SwiftUIAttributes`](attributescopes/swiftuiattributes.md), and [`AttributeScopes.AccessibilityAttributes`](attributescopes/accessibilityattributes.md). To use third-party attribute scopes, use the initializers [`init(_:including:)`](attributedstring/init(_:including:)-9no47.md) or [`init(_:including:)`](attributedstring/init(_:including:)-puv0.md).

## Parameters

- `nsStr`: The   to convert.

## See Also

- [init<S>(NSAttributedString, including: S.Type) throws](attributedstring/init(_:including:)-9no47.md)
  Creates a value-type attributed string from a reference type, including an attribute scope.
- [init<S>(NSAttributedString, including: KeyPath<AttributeScopes, S.Type>) throws](attributedstring/init(_:including:)-puv0.md)
  Creates a value-type attributed string from a reference type, including an attribute scope that a key path identifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(_:)-1fru0)*