# transformingAttributes(_:_:)

**Framework**: Foundation  
**Kind**: method

Returns an attributed string by calling a closure that transforms one attribute, which a key path identifies, of a source attributed string.

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
func transformingAttributes<K>(_ k: KeyPath<AttributeDynamicLookup, K>, _ c: (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString where K : AttributedStringKey, K.Value : Sendable
```

#### Return Value

An attributed string with the applied transformation to the specified attribute.

## Parameters

- `k`: The key path to the   that identifies the attribute to transform.
- `c`: The closure that receives an   that you use to access and alter the attribute’s range and value.

## See Also

- [func transformingAttributes<K>(K.Type, (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:)-9prm2.md)
  Returns an attributed string by calling a closure that transforms one attribute of a source attributed string.
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
- [func transformingAttributes<K1, K2, K3, K4, K5>(K1.Type, K2.Type, K3.Type, K4.Type, K5.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:_:)-3i7ac.md)
  Returns an attributed string created by calling a closure that transforms five attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4, K5>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, KeyPath<AttributeDynamicLookup, K4>, KeyPath<AttributeDynamicLookup, K5>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:_:)-9hppo.md)
  Returns an attributed string created by calling a closure that transforms five attributes, which key paths identify, of a source attributed string.
- [AttributedString.SingleAttributeTransformer](attributedstring/singleattributetransformer.md)
  A type that transforms an attribute by altering its range or value, or by replacing it entirely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transformingattributes(_:_:)-64qnl)*