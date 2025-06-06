# MaskStorage

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

The mask type resulting from pointwise comparisons of this vector type.

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
associatedtype MaskStorage : SIMD where Self.MaskStorage.Scalar : FixedWidthInteger, Self.MaskStorage.Scalar : SignedInteger
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd/maskstorage)*