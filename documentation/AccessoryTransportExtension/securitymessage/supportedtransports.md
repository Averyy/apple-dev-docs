# supportedTransports

**Framework**: Accessory Transport Extension  
**Kind**: property

An array of transports the accessory supports for sending sensitive information.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
let supportedTransports: [AccessoryTransport]
```

#### Discussion

The default is [`AccessoryTransport.bluetooth`](accessorytransport/bluetooth.md) only. To support [`AccessoryTransport.internet`](accessorytransport/internet.md) or [`AccessoryTransport.localNetwork`](accessorytransport/localnetwork.md), you must use [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) for enhanced security.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/supportedtransports)*