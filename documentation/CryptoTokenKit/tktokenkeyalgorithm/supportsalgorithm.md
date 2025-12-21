# supportsAlgorithm(_:)

**Framework**: CryptoTokenKit  
**Kind**: method

Whether the specified algorithm is the target operation algorithm, or one of the other algorithms used.

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
func supportsAlgorithm(_ algorithm: SecKeyAlgorithm) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `algorithm` is the target operation algorithm or one of the other algorithms used; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `algorithm`: The algorithm to be checked.

## See Also

- [func isAlgorithm(SecKeyAlgorithm) -> Bool](tktokenkeyalgorithm/isalgorithm(_:).md)
  Returns whether the specified algorithm is the target operation algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyalgorithm/supportsalgorithm(_:))*