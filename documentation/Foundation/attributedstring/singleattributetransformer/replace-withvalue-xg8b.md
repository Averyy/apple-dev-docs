# replace(with:value:)

**Framework**: Foundation  
**Kind**: method

Replaces an attribute with a different attribute that a key path identifies.

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
mutating func replace<U>(with keyPath: KeyPath<AttributeDynamicLookup, U>, value: U.Value) where U : AttributedStringKey, U.Value : Sendable
```

## Parameters

- `keyPath`: The key path that identifies the new attribute.
- `value`: The value of the new attribute.

## See Also

- [func replace<U>(with: U.Type, value: U.Value)](attributedstring/singleattributetransformer/replace(with:value:)-6bn0e.md)
  Replaces an attribute with a different attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/singleattributetransformer/replace(with:value:)-xg8b)*