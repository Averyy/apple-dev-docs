# MTRKeypair

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
protocol MTRKeypair : NSObjectProtocol
```

```objc
@protocol MTRKeypair <NSObject>
```

## Mentions

- [Onboarding a Matter device](./onboarding-a-matter-device.md)

## Topics

### Instance Methods
- [func publicKey() -> Unmanaged<SecKey>](./mtrkeypair/publickey%28%29.md)
- [func signMessageECDSA_DER(Data) -> Data](./mtrkeypair/signmessageecdsa_der%28_%29.md)
- [func signMessageECDSA_RAW(Data) -> Data](./mtrkeypair/signmessageecdsa_raw%28_%29.md)
- [func copyPublicKey() -> SecKey](./mtrkeypair/copypublickey%28%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrkeypair)*