# replacing(with:where:)

**Framework**: Swift  
**Kind**: method

Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.

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
func replacing(with other: Self, where mask: SIMDMask<Self.MaskStorage>) -> Self
```

#### Discussion

Equivalent to:

```swift
var result = Self()
for i in indices {
  result[i] = mask[i] ? other[i] : self[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd3/replacing(with:where:)-32h3i)*