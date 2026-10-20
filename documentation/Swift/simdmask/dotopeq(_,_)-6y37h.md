# .^=(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Replaces `a` with the pointwise exclusive or of `a` and `b`.

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
static func .^= (a: inout SIMDMask<Storage>, b: SIMDMask<Storage>)
```

Available when `Storage` conforms to `SIMD`, `Storage.Scalar` conforms to `FixedWidthInteger`, and `Storage.Scalar` conforms to `SignedInteger`.

#### Discussion

Equivalent to:

```swift
for i in a.indices {
  a[i] = a[i] != b[i]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/'._=(_:_:)-6y37h)*