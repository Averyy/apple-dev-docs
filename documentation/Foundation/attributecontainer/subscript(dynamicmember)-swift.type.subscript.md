# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript  
**Role**: Type Subscript

Returns a modified attribute container as part of building a chain of attributes, for use as a static method.

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
static subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K> where K : AttributedStringKey { get }
```

#### Discussion

This method returns an [`AttributeContainer.Builder`](./builder.md), which allows you to chain multiple attributes in a single call, like this:

```swift
// An attribute container with the link and backgroundColor attributes.
let myContainer = AttributeContainer.link(myURL).backgroundColor(.yellow)
```

## See Also

### Accessing Attributes
- [subscript<T>(T.Type) -> T.Value?](./subscript%28_%29.md)
  Returns the attribute that corresponds to a specified key.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](./subscript%28dynamicmember%29-657oj.md)
  Returns the attribute that corresponds to a specified key path.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](./subscript%28dynamicmember%29-3jcvx.md)
  Returns the attribute container that corresponds to a specified key path.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K>](./subscript%28dynamicmember%29-60ps5.md)
  Returns a modified attribute container as part of building a chain of attributes.
- [protocol AttributedStringKey](../attributedstringkey.md)
  A type that defines an attribute’s name and type.
- [AttributeContainer.Builder](./builder.md)
  A type that iteratively builds attribute containers by setting attribute values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/subscript(dynamicmember:)-swift.type.subscript)*