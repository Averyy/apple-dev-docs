# supportsAlgorithm(_:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) supportsAlgorithm:(SecKeyAlgorithm) algorithm;
```

## Return Value

[`true`](../../Swift/true.md) if `algorithm` is the target operation algorithm or one of the other algorithms used; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `algorithm`: The algorithm to be checked.

## See Also

### Determining Algorithm Usage
- [func isAlgorithm(SecKeyAlgorithm) -> Bool](./isalgorithm%28_%29.md)
  Returns whether the specified algorithm is the target operation algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyalgorithm/supportsalgorithm(_:))*