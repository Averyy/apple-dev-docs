# .!=(_:_:)

**Framework**: Swift  
**Kind**: op

Pointwise compare not equal to.

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
static func .!= (a: SIMD2<Scalar>, b: SIMD2<Scalar>) -> SIMDMask<SIMD2<Scalar>.MaskStorage>
```

#### Discussion

Each lane of the result is true if that lane of a is not equal to the corresponding lane of b, and false otherwise.

Equivalent to:

```swift
var result = SIMDMask<MaskStorage>()
for i in 0..<2 {
  result[i] = (a[i] != b[i])
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd2/'.!=(_:_:)-4hwla)*