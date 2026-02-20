# .>=(_:_:)

**Framework**: Swift  
**Kind**: op

Pointwise compare greater than or equal to.

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
static func .>= (a: SIMD64<Scalar>, b: Scalar) -> SIMDMask<SIMD64<Scalar>.MaskStorage>
```

#### Discussion

Each lane of the result is true if that lane of a is greater than or equal to b, and false otherwise.

Equivalent to:

```swift
var result = SIMDMask<MaskStorage>()
for i in 0..<64 {
  result[i] = (a[i] >= b)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd64/'._=(_:_:)-1vb8h)*