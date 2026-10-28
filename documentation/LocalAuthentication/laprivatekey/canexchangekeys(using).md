# canExchangeKeys(using:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Checks whether the algorithm you supply is valid for performing key exchanges.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func canExchangeKeys(using algorithm: SecKeyAlgorithm) -> Bool
```

```objc
- (BOOL) canExchangeKeysUsingSecKeyAlgorithm:(SecKeyAlgorithm) algorithm;
```

## Return Value

A Boolean value that indicates whether the algorithm you supply is valid for performing key exchanges.

## Parameters

- `algorithm`: A cryptographic algorithm.

## See Also

### Checking algorithm support
- [func canDecrypt(using: SecKeyAlgorithm) -> Bool](./candecrypt%28using%29.md)
  Checks whether the algorithm you supply is valid for decrypting data with the key.
- [func canSign(using: SecKeyAlgorithm) -> Bool](./cansign%28using%29.md)
  Checks whether the algorithm you supply is valid for signing data with the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laprivatekey/canexchangekeys(using:))*