# isAlgorithm(_:)

**Framework**: CryptoTokenKit  
**Kind**: method

Returns whether the specified algorithm is the target operation algorithm.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func isAlgorithm(_ algorithm: SecKeyAlgorithm) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `algorithm` is the target operation algorithm; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `algorithm`: The algorithm to be checked.

## See Also

- [func supportsAlgorithm(SecKeyAlgorithm) -> Bool](tktokenkeyalgorithm/supportsalgorithm(_:).md)
  Whether the specified algorithm is the target operation algorithm, or one of the other algorithms used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyalgorithm/isalgorithm(_:))*