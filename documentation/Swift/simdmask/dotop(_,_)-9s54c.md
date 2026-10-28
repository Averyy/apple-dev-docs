# .^(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

A vector mask that is the pointwise exclusive or of the inputs.

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
static func .^ (a: SIMDMask<Storage>, b: SIMDMask<Storage>) -> SIMDMask<Storage>
```

Available when `Storage` is `SIMD16<Int64>`.

## Discussion

Equivalent to:

```swift
var result = SIMDMask<SIMD16<Int64>>()
for i in result.indices {
  result[i] = a[i] != b[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/'._(_:_:)-9s54c)*