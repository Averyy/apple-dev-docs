# replace(with:where:)

**Framework**: Swift  
**Kind**: method

Replaces elements of this vector with `other` in the lanes where `mask` is `true`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func replace(with other: Self.Scalar, where mask: SIMDMask<Self.MaskStorage>)
```

#### Discussion

Equivalent to:

```swift
for i in indices {
  if mask[i] { self[i] = other }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd16/replace(with:where:)-9cks4)*