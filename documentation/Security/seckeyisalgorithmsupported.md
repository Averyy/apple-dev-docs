# SecKeyIsAlgorithmSupported(_:_:_:)

**Framework**: Security  
**Kind**: func

Returns a Boolean indicating whether a key is suitable for an operation using a certain algorithm.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func SecKeyIsAlgorithmSupported(_ key: SecKey, _ operation: SecKeyOperationType, _ algorithm: SecKeyAlgorithm) -> Bool
```

## Mentions

- [Signing and Verifying](signing-and-verifying.md)
- [Using Keys for Encryption](using-keys-for-encryption.md)

#### Return Value

A Boolean indicating whether the key can be used for the given operation and algorithm.

## Parameters

- `key`: The key whose suitability you want to test.
- `operation`: The operation that you want to perform with the key. Use one of the values from  .
- `algorithm`: The algorithm that you want to perform with the key. Use one of the values from  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyisalgorithmsupported(_:_:_:))*