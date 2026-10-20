# .&(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

A vector mask that is the pointwise logical conjunction of the inputs.

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
static func .& (a: Bool, b: SIMDMask<Storage>) -> SIMDMask<Storage>
```

Available when `Storage` conforms to `SIMD`, `Storage.Scalar` conforms to `FixedWidthInteger`, and `Storage.Scalar` conforms to `SignedInteger`.

#### Discussion

Equivalent to `a ? b : SIMDMask(repeating: false)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/'.&(_:_:)-20xdw)*