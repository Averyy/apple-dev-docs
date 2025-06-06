# !=(_:_:)

**Framework**: RealityKit  
**Kind**: op

Returns a Boolean value indicating whether two values are not equal.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

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

- [var hashValue: Int](custommaterial/lightingmodel-swift.enum/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](custommaterial/lightingmodel-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func == (CustomMaterial.LightingModel, CustomMaterial.LightingModel) -> Bool](custommaterial/lightingmodel-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/lightingmodel-swift.enum/!=(_:_:))*