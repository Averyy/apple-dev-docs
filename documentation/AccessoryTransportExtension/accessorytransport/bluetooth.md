# AccessoryTransport.bluetooth

**Framework**: Accessory Transport Extension  
**Kind**: case

A transport method that uses Bluetooth for data delivery.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
case bluetooth
```

#### Discussion

This transport method prefers [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) cryptography, but supports [`SecurityMessage.CipherSuite.p256`](securitymessage/ciphersuite-swift.enum/p256.md) as a fallback. The system prioritizes this transport method when the accessory connection is active.

## See Also

- [AccessoryTransport.internet](accessorytransport/internet.md)
  A transport method that uses the internet for data delivery.
- [AccessoryTransport.localNetwork](accessorytransport/localnetwork.md)
  A transport method that uses the local network for data delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransport/bluetooth)*