# canDecrypt(using:)

**Framework**: Local Authentication  
**Kind**: method

Checks whether the algorithm you supply is valid for decrypting data with the key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func canDecrypt(using algorithm: SecKeyAlgorithm) -> Bool
```

#### Return Value

A Boolean value that indicates whether the algorithm you supply is valid for decrypting data with the key.

## Parameters

- `algorithm`: A cryptographic algorithm.

## See Also

- [func canExchangeKeys(using: SecKeyAlgorithm) -> Bool](laprivatekey/canexchangekeys(using:).md)
  Checks whether the algorithm you supply is valid for performing key exchanges.
- [func canSign(using: SecKeyAlgorithm) -> Bool](laprivatekey/cansign(using:).md)
  Checks whether the algorithm you supply is valid for signing data with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laprivatekey/candecrypt(using:))*