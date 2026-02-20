# .<(_:_:)

**Framework**: Swift  
**Kind**: op

Pointwise compare less than.

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
static func .< (a: Scalar, b: SIMD3<Scalar>) -> SIMDMask<SIMD3<Scalar>.MaskStorage>
```

#### Discussion

Each lane of the result is true if a is less than the corresponding lane of b, and false otherwise.

Equivalent to:

```swift
var result = SIMDMask<MaskStorage>()
for i in 0..<3 {
  result[i] = (a < b[i])
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd3/'._(_:_:)-3mqbw)*