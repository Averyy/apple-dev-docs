# .!=(_:_:)

**Framework**: Swift  
**Kind**: op

Pointwise compare not equal to.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static func .!= (a: Scalar, b: SIMD32<Scalar>) -> SIMDMask<SIMD32<Scalar>.MaskStorage>
```

#### Discussion

Each lane of the result is true if a is not equal to the corresponding lane of b, and false otherwise.

Equivalent to:

```swift
var result = SIMDMask<MaskStorage>()
for i in 0..<32 {
  result[i] = (a != b[i])
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd32/'.!=(_:_:)-5lukx)*