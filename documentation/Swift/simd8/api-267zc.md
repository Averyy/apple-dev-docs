# .==(_:_:)

**Framework**: Swift  
**Kind**: op

Pointwise compare equal to.

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
static func .== (a: SIMD8<Scalar>, b: SIMD8<Scalar>) -> SIMDMask<SIMD8<Scalar>.MaskStorage>
```

#### Discussion

Each lane of the result is true if that lane of a is equal to the corresponding lane of b, and false otherwise.

Equivalent to:

```swift
var result = SIMDMask<MaskStorage>()
for i in 0..<8 {
  result[i] = (a[i] == b[i])
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd8/'.==(_:_:)-267zc)*