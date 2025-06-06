# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Returns the attributed string key for a specified AppKit key path.

**Availability**:
- macOS 12.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.AppKitAttributes, T>) -> T where T : AttributedStringKey { get }
```

## See Also

- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.FoundationAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3nor6.md)
  Returns the attributed string key for a specified Foundation key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.FoundationAttributes.NumberFormatAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3neai.md)
  Returns the attributed string key for a specified Foundation number format key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.SwiftUIAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-3q4ap.md)
  Returns the attributed string key for a specified SwiftUI key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.UIKitAttributes, T>) -> T](attributedynamiclookup/subscript(dynamicmember:)-4yyyo.md)
  Returns the attributed string key for a specified UIKit key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-3v1cn)*