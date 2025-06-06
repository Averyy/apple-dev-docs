# !=(_:_:)

**Framework**: RealityKit  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
static func != (lhs: Self, rhs: Self) -> Bool
```

#### Discussion

Inequality is the inverse of equality. For any values `a` and `b`, `a != b` implies that `a == b` is `false`.

This is the default implementation of the not-equal-to operator (`!=`) for any type that conforms to `Equatable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.

## See Also

- [var hashValue: Int](textureresource/mipmapsmode/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](textureresource/mipmapsmode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func == (TextureResource.MipmapsMode, TextureResource.MipmapsMode) -> Bool](textureresource/mipmapsmode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/mipmapsmode/!=(_:_:))*