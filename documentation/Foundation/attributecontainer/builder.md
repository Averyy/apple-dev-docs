# AttributeContainer.Builder

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that iteratively builds attribute containers by setting attribute values.

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
struct Builder<T> where T : AttributedStringKey
```

#### Overview

The [`AttributeContainer.Builder`](./builder.md) type lets you build [`AttributeContainer`](../attributecontainer.md) instances by chaining together several attributes in one expression. The following example shows this approach:

```swift
// An attribute container with the link and backgroundColor attributes.
let myContainer = AttributeContainer().link(myURL).backgroundColor(.yellow)
```

The first part of this expression, `AttributeContainer().link(URL(myURL))`, creates a builder to apply the [`link`](../attributescopes/foundationattributes/link.md) attribute to the empty [`AttributeContainer`](../attributecontainer.md). The builder’s [`callAsFunction(_:)`](./builder/callasfunction%28_%29.md) returns a new [`AttributeContainer`](../attributecontainer.md) with this attribute set. Then the `backgroundColor(.yellow)` creates a second builder to modify the just-returned [`AttributeContainer`](../attributecontainer.md) by adding the [`backgroundColor`](../attributescopes/swiftuiattributes/backgroundcolor.md) attribute. The result is an [`AttributeContainer`](../attributecontainer.md) with both attributes set.

## Topics

### Calling Builder Functions
- [func callAsFunction(T.Value) -> AttributeContainer](./builder/callasfunction%28_%29.md)
  Builds an attribute container by setting an attribute and returning a modified attribute container.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [static subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> AttributeContainer.Builder<K>](./subscript%28dynamicmember%29-swift.type.subscript.md)
  Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [protocol AttributedStringKey](../attributedstringkey.md)
  A type that defines an attribute’s name and type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/builder)*