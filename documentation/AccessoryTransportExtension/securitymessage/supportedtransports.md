# supportedTransports

**Framework**: Accessory Transport Extension  
**Kind**: property

An array of transports that the accessory supports for sending sensitive information.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
let supportedTransports: [AccessoryTransport]
```

#### Discussion

The default is [`AccessoryTransport.bluetooth`](accessorytransport/bluetooth.md). To support the [`AccessoryTransport.internet`](accessorytransport/internet.md) or [`AccessoryTransport.localNetwork`](accessorytransport/localnetwork.md) transport types, use the [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) cipher suite.

> **Note**: Specify all transports your accessory supports when initiating key exchange. The system automatically selects the best available transport for each message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/supportedtransports)*