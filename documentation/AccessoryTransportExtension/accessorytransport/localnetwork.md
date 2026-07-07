# AccessoryTransport.localNetwork

**Framework**: Accessory Transport Extension  
**Kind**: case

A transport method that uses the local network for data delivery.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
case localNetwork
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

The system requires [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) cryptography for this transport method.

## See Also

- [AccessoryTransport.bluetooth](accessorytransport/bluetooth.md)
  A transport method that uses Bluetooth for data delivery.
- [AccessoryTransport.internet](accessorytransport/internet.md)
  A transport method that uses the internet for data delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransport/localnetwork)*