# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Returns the attribute container that corresponds to a specified key path.

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

Use this subscript when you need to work with an explicit attribute scope. For example, the SwiftUI [`foregroundColor`](attributescopes/swiftuiattributes/foregroundcolor.md) attribute overrides the attribute in the AppKit and UIKit scopes with the same name. If you work with both the SwiftUI and UIKit scopes, you can use the syntax `myAttributeContainer.uiKit.foregroundColor` to disambiguate and explicitly use the UIKit attribute.

## See Also

- [subscript<T>(T.Type) -> T.Value?](attributecontainer/subscript(_:).md)
  Returns the attribute that corresponds to a specified key.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributecontainer/subscript(dynamicmember:)-657oj.md)
  Returns the attribute that corresponds to a specified key path.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K>](attributecontainer/subscript(dynamicmember:)-60ps5.md)
  Returns a modified attribute container as part of building a chain of attributes.
- [static subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K>](attributecontainer/subscript(dynamicmember:)-swift.type.subscript.md)
  Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [protocol AttributedStringKey](attributedstringkey.md)
  A type that defines an attribute’s name and type.
- [AttributeContainer.Builder](attributecontainer/builder.md)
  A type that iteratively builds attribute containers by setting attribute values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/subscript(dynamicmember:)-3jcvx)*