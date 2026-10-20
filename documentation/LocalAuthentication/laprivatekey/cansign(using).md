# canSign(using:)

**Framework**: Local Authentication  
**Kind**: method  
**Role**: Instance Method

Checks whether the algorithm you supply is valid for signing data with the key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func canSign(using algorithm: SecKeyAlgorithm) -> Bool
```

```objc
- (BOOL) canSignUsingSecKeyAlgorithm:(SecKeyAlgorithm) algorithm;
```

#### Return Value

A Boolean value that indicates whether the algorithm you supply is valid for signing data with the key.

## Parameters

- `algorithm`: A cryptographic algorithm.

## See Also

### Checking algorithm support
- [func canDecrypt(using: SecKeyAlgorithm) -> Bool](./candecrypt%28using%29.md)
  Checks whether the algorithm you supply is valid for decrypting data with the key.
- [func canExchangeKeys(using: SecKeyAlgorithm) -> Bool](./canexchangekeys%28using%29.md)
  Checks whether the algorithm you supply is valid for performing key exchanges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laprivatekey/cansign(using:))*