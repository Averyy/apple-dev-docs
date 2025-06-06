# canVerify(using:)

**Framework**: Local Authentication  
**Kind**: method

Checks whether the algorithm you supply is valid for verifying signatures with the key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func canVerify(using algorithm: SecKeyAlgorithm) -> Bool
```

#### Return Value

A Boolean value that indicates whether the algorithm you supply is valid for verifying signatures with the key.

## Parameters

- `algorithm`: A cryptographic algorithm.

## See Also

- [func canEncrypt(using: SecKeyAlgorithm) -> Bool](lapublickey/canencrypt(using:).md)
  Checks whether the algorithm you supply is valid for encrypting data with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapublickey/canverify(using:))*