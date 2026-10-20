# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the attributed string key for a specified UIKit key path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.UIKitAttributes, T>) -> T where T : AttributedStringKey { get }
```

## See Also

### Accessing Framework Attribute Scopes
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.FoundationAttributes, T>) -> T](./subscript%28dynamicmember%29-3nor6.md)
  Returns the attributed string key for a specified Foundation key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.FoundationAttributes.NumberFormatAttributes, T>) -> T](./subscript%28dynamicmember%29-3neai.md)
  Returns the attributed string key for a specified Foundation number format key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.SwiftUIAttributes, T>) -> T](./subscript%28dynamicmember%29-3q4ap.md)
  Returns the attributed string key for a specified SwiftUI key path.
- [subscript<T>(dynamicMember _: KeyPath<AttributeScopes.AppKitAttributes, T>) -> T](./subscript%28dynamicmember%29-3v1cn.md)
  Returns the attributed string key for a specified AppKit key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-4yyyo)*