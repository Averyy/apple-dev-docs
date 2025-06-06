# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates a reference-type attributed string from the specified value-type attributed string.

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
convenience init(_ attrStr: AttributedString)
```

#### Discussion

This initializer includes all attribute scopes defined by the SDK, such as [`AttributeScopes.FoundationAttributes`](attributescopes/foundationattributes.md), [`AttributeScopes.SwiftUIAttributes`](attributescopes/swiftuiattributes.md), and [`AttributeScopes.AccessibilityAttributes`](attributescopes/accessibilityattributes.md). To use third-party attribute scopes, use the initializers [`init(_:including:)`](nsattributedstring/init(_:including:)-9gogq.md) or [`init(_:including:)`](nsattributedstring/init(_:including:)-8iy4i.md).

## Parameters

- `attrStr`: The value type attributed string that provides the text and attributes of the new object.

## See Also

- [convenience init<S>(AttributedString, including: S.Type) throws](nsattributedstring/init(_:including:)-9gogq.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.
- [convenience init<S>(AttributedString, including: KeyPath<AttributeScopes, S.Type>) throws](nsattributedstring/init(_:including:)-8iy4i.md)
  Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(_:))*