# SecKeyCopyKeyExchangeResult(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Performs the Diffie-Hellman style of key exchange with optional key-derivation steps.

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
func SecKeyCopyKeyExchangeResult(_ privateKey: SecKey, _ algorithm: SecKeyAlgorithm, _ publicKey: SecKey, _ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?
```

#### Return Value

A data object representing the result of the key exchange operation or `NULL` on failure. In Objective-C, call [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) to free the data object’s memory when you are done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycopykeyexchangeresult(_:_:_:_:_:))*