# .==(_:_:)

**Framework**: Swift  
**Kind**: op

A vector mask with the result of a pointwise equality comparison.

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
static func .== (a: SIMDMask<Storage>, b: SIMDMask<Storage>) -> SIMDMask<Storage>
```

#### Discussion

Equivalent to:

```swift
var result = SIMDMask<SIMD8<Int64>>()
for i in result.indices {
  result[i] = a[i] == b[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/'.==(_:_:)-6cck1)*