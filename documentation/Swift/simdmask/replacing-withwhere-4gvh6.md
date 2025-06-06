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
func replacing(with other: SIMDMask<Storage>, where mask: SIMDMask<Storage>) -> SIMDMask<Storage>
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/replacing(with:where:)-4gvh6)*