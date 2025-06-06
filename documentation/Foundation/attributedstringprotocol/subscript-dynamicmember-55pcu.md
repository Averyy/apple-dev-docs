# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript  
**Required**: Yes

Returns a scoped attribute container that a key path indicates.

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
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S> where S : AttributeScope { get set }
```

#### Discussion

Use this subscript when you need to work with an explicit attribute scope. For example, the SwiftUI [`foregroundColor`](attributescopes/swiftuiattributes/foregroundcolor.md) attribute overrides the attribute in the AppKit and UIKit scopes with the same name. If you work with both the SwiftUI and UIKit scopes, you can use the syntax `myAttributedString.uiKit.foregroundColor` to disambiguate and explicitly use the UIKit attribute.

The attribute container that this method returns contains only attributes that exist, and are present and identical for the entire attributed string. To find portions of the string with consistent attributes, use the [`runs`](attributedstringprotocol/runs.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## See Also

- [subscript<K>(K.Type) -> K.Value?](attributedstringprotocol/subscript(_:)-4thnp.md)
  Returns an attribute value that corresponds to an attributed string key.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributedstringprotocol/subscript(dynamicmember:)-2wake.md)
  Returns an attribute value that a key path indicates.
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(dynamicmember:)-55pcu)*