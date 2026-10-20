# .>(_:_:)

**Framework**: Swift  
**Kind**: op

Pointwise compare greater than.

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
static func .> (a: Scalar, b: SIMD16<Scalar>) -> SIMDMask<SIMD16<Scalar>.MaskStorage>
```

#### Discussion

Each lane of the result is true if a is greater than the corresponding lane of b, and false otherwise.

Equivalent to:

```swift
var result = SIMDMask<MaskStorage>()
for i in 0..<16 {
  result[i] = (a > b[i])
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd16/'._(_:_:)-2s9fi)*