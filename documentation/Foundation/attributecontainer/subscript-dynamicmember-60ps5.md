# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Returns a modified attribute container as part of building a chain of attributes.

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
subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K> where K : AttributedStringKey { get }
```

#### Discussion

This method returns an [`AttributeContainer.Builder`](attributecontainer/builder.md), which allows you to chain multiple attributes in a single call, like this:

```swift
// An attribute container with the link and backgroundColor attributes.
let myContainer = AttributeContainer().link(myURL).backgroundColor(.yellow)
```

## See Also

- [subscript<T>(T.Type) -> T.Value?](attributecontainer/subscript(_:).md)
  Returns the attribute that corresponds to a specified key.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributecontainer/subscript(dynamicmember:)-657oj.md)
  Returns the attribute that corresponds to a specified key path.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](attributecontainer/subscript(dynamicmember:)-3jcvx.md)
  Returns the attribute container that corresponds to a specified key path.
- [static subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K>](attributecontainer/subscript(dynamicmember:)-swift.type.subscript.md)
  Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [protocol AttributedStringKey](attributedstringkey.md)
  A type that defines an attribute’s name and type.
- [AttributeContainer.Builder](attributecontainer/builder.md)
  A type that iteratively builds attribute containers by setting attribute values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/subscript(dynamicmember:)-60ps5)*