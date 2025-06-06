# ==(_:_:)

**Framework**: Apple CryptoKit  
**Kind**: op

Determines whether a digest is equivalent to a collection of contiguous bytes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func == <D>(lhs: Self, rhs: D) -> Bool where D : DataProtocol
```

#### Return Value

A Boolean value that’s `true` if the digest is equivalent to the collection of binary data.

## Parameters

- `lhs`: A digest to compare.
- `rhs`: A collection of contiguous bytes to compare.

## See Also

- [static func == (Self, Self) -> Bool](digest/==(_:_:)-6m59k.md)
  Determines whether two digests are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/digest/==(_:_:)-7yz3z)*