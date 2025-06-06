# transformingAttributes(_:_:_:_:_:_:)

**Framework**: Foundation  
**Kind**: method

Returns an attributed string created by calling a closure that transforms five attributes of a source attributed string.

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
func transformingAttributes<K1, K2, K3, K4, K5>(_ k: K1.Type, _ k2: K2.Type, _ k3: K3.Type, _ k4: K4.Type, _ k5: K5.Type, _ c: (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString where K1 : AttributedStringKey, K2 : AttributedStringKey, K3 : AttributedStringKey, K4 : AttributedStringKey, K5 : AttributedStringKey, K1.Value : Sendable, K2.Value : Sendable, K3.Value : Sendable, K4.Value : Sendable, K5.Value : Sendable
```

#### Return Value

An attributed string with the applied transformations to the specified attributes.

## Parameters

- `k`: The   that identifies an attribute to transform.
- `k2`: The   that identifies a second attribute to transform.
- `k3`: The   that identifies a third attribute to transform.
- `k4`: The   that identifies a fourth attribute to transform.
- `k5`: The   that identifies a fifth attribute to transform.
- `c`: A closure that receives four   instances that you use to access and alter the attributes’ ranges and values.

## See Also

- [func transformingAttributes<K>(K.Type, (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:)-9prm2.md)
  Returns an attributed string by calling a closure that transforms one attribute of a source attributed string.
- [func transformingAttributes<K>(KeyPath<AttributeDynamicLookup, K>, (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:)-64qnl.md)
  Returns an attributed string by calling a closure that transforms one attribute, which a key path identifies, of a source attributed string.
- [func transformingAttributes<K1, K2>(K1.Type, K2.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:)-7kw1o.md)
  Returns an attributed string by calling a closure that transforms two attributes of a source attributed string.
- [func transformingAttributes<K1, K2>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:)-8gt2n.md)
  Returns an attributed string created by calling a closure that transforms two attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3>(K1.Type, K2.Type, K3.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:)-4owv7.md)
  Returns an attributed string by calling a closure that transforms three attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:)-5xmlf.md)
  Returns an attributed string by calling a closure that transforms three attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4>(K1.Type, K2.Type, K3.Type, K4.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:)-9uodg.md)
  Returns an attributed string by calling a closure that transforms four attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, KeyPath<AttributeDynamicLookup, K4>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:)-all0.md)
  Returns an attributed string created by calling a closure that transforms four attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4, K5>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, KeyPath<AttributeDynamicLookup, K4>, KeyPath<AttributeDynamicLookup, K5>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:_:)-9hppo.md)
  Returns an attributed string created by calling a closure that transforms five attributes, which key paths identify, of a source attributed string.
- [AttributedString.SingleAttributeTransformer](attributedstring/singleattributetransformer.md)
  A type that transforms an attribute by altering its range or value, or by replacing it entirely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transformingattributes(_:_:_:_:_:_:)-3i7ac)*