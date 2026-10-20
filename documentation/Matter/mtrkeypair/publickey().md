# publicKey()

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 18.4
- iPadOS 16.1+ - Deprecated in 18.4
- Mac Catalyst 16.1+ - Deprecated in 18.4
- macOS 13.0+ - Deprecated in 15.4
- tvOS 16.1+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 9.1+ - Deprecated in 11.4

> **Deprecated**: Please implement copyPublicKey, this will leak otherwise

## Declaration

```swift
optional func publicKey() -> Unmanaged<SecKey>
```

```objc
- (SecKeyRef) publicKey;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrkeypair/publickey())*