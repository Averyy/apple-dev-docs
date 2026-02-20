# .>(_:_:)

**Framework**: Swift  
**Kind**: op

Pointwise compare greater than.

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
static func .> (a: SIMD3<Scalar>, b: Scalar) -> SIMDMask<SIMD3<Scalar>.MaskStorage>
```

#### Discussion

Each lane of the result is true if that lane of a is greater than b, and false otherwise.

Equivalent to:

```swift
var result = SIMDMask<MaskStorage>()
for i in 0..<3 {
  result[i] = (a[i] > b)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd3/'._(_:_:)-2j6hl)*