# SecurityMessage.CipherSuite.xWing

**Framework**: Accessory Transport Extension  
**Kind**: case

A cipher suite that provides xWing hybrid post-quantum key encapsulation.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
case xWing
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

Implement this cipher suite for post-quantum security. The [`AccessoryTransport.internet`](accessorytransport/internet.md) and [`AccessoryTransport.localNetwork`](accessorytransport/localnetwork.md) transport types require this cipher suite. Bluetooth transport supports this cipher suite, but you can alternatively use [`SecurityMessage.CipherSuite.p256`](securitymessage/ciphersuite-swift.enum/p256.md) as a fallback.

## See Also

- [SecurityMessage.CipherSuite.p256](securitymessage/ciphersuite-swift.enum/p256.md)
  A cipher suite that uses NIST P-256 elliptic curve cryptography.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/ciphersuite-swift.enum/xwing)*