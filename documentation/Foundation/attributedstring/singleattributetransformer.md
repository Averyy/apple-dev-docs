# AttributedString.SingleAttributeTransformer

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that transforms an attribute by altering its range or value, or by replacing it entirely.

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
@preconcurrency
struct SingleAttributeTransformer<T> where T : AttributedStringKey, T.Value : Sendable
```

#### Overview

For simple transformations, the closure you provide to the `transformingAttributes(…)` methods of [`AttributedString`](../attributedstring.md) can use this instance to change the attribute’s value. You can also use this instance to change the range of the string that the attribute applies to. To completely replace the attribute with an attribute of a different type, use [`replace(with:value:)`](./singleattributetransformer/replace%28with,value%29-6bn0e.md).

## Topics

### Accessing the Attribute’s Range
- [var range: Range<AttributedString.Index>](./singleattributetransformer/range.md)
  The range of the attribute in the attributed string.
### Accessing the Attribute’s Value
- [var value: T.Value?](./singleattributetransformer/value.md)
  The value of the attribute.
### Replacing Attributes
- [func replace<U>(with: U.Type, value: U.Value)](./singleattributetransformer/replace%28with,value%29-6bn0e.md)
  Replaces an attribute with a different attribute.
- [func replace<U>(with: KeyPath<AttributeDynamicLookup, U>, value: U.Value)](./singleattributetransformer/replace%28with,value%29-xg8b.md)
  Replaces an attribute with a different attribute that a key path identifies.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Transforming Attributes
- [func transformingAttributes<K>(K.Type, (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString](./transformingattributes%28_,_%29-9prm2.md)
  Returns an attributed string by calling a closure that transforms one attribute of a source attributed string.
- [func transformingAttributes<K>(KeyPath<AttributeDynamicLookup, K>, (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString](./transformingattributes%28_,_%29-64qnl.md)
  Returns an attributed string by calling a closure that transforms one attribute, which a key path identifies, of a source attributed string.
- [func transformingAttributes<K1, K2>(K1.Type, K2.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>) -> Void) -> AttributedString](./transformingattributes%28_,_,_%29-7kw1o.md)
  Returns an attributed string by calling a closure that transforms two attributes of a source attributed string.
- [func transformingAttributes<K1, K2>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>) -> Void) -> AttributedString](./transformingattributes%28_,_,_%29-8gt2n.md)
  Returns an attributed string created by calling a closure that transforms two attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3>(K1.Type, K2.Type, K3.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>) -> Void) -> AttributedString](./transformingattributes%28_,_,_,_%29-4owv7.md)
  Returns an attributed string by calling a closure that transforms three attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>) -> Void) -> AttributedString](./transformingattributes%28_,_,_,_%29-5xmlf.md)
  Returns an attributed string by calling a closure that transforms three attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4>(K1.Type, K2.Type, K3.Type, K4.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>) -> Void) -> AttributedString](./transformingattributes%28_,_,_,_,_%29-9uodg.md)
  Returns an attributed string by calling a closure that transforms four attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, KeyPath<AttributeDynamicLookup, K4>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>) -> Void) -> AttributedString](./transformingattributes%28_,_,_,_,_%29-all0.md)
  Returns an attributed string created by calling a closure that transforms four attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4, K5>(K1.Type, K2.Type, K3.Type, K4.Type, K5.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString](./transformingattributes%28_,_,_,_,_,_%29-3i7ac.md)
  Returns an attributed string created by calling a closure that transforms five attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4, K5>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, KeyPath<AttributeDynamicLookup, K4>, KeyPath<AttributeDynamicLookup, K5>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString](./transformingattributes%28_,_,_,_,_,_%29-9hppo.md)
  Returns an attributed string created by calling a closure that transforms five attributes, which key paths identify, of a source attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/singleattributetransformer)*