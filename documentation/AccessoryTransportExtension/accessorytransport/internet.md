# AccessoryTransport.internet

**Framework**: Accessory Transport Extension  
**Kind**: case

A transport method that uses the internet for data delivery.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
case internet
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

The system requires [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) cryptography for this transport method. The system tries this transport method if Bluetooth and local network are unavailable.

> **Note**: Internet transport uses a different encryption mechanism than Bluetooth. The system handles encryption and decryption transparently using Symmetric Key Ratchet derivation from the initial key exchange.

## See Also

- [AccessoryTransport.bluetooth](accessorytransport/bluetooth.md)
  A transport method that uses Bluetooth for data delivery.
- [AccessoryTransport.localNetwork](accessorytransport/localnetwork.md)
  A transport method that uses the local network for data delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransport/internet)*