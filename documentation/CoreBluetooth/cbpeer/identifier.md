# identifier

**Framework**: Core Bluetooth  
**Kind**: property

The UUID associated with the peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var identifier: UUID { get }
```

#### Discussion

The value of this property represents the unique identifier of the peer. The first time a local manager encounters a peer, the system assigns the peer a UUID, represented by a new [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) object. Peers use [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) instances to identify themselves, instead of by the [`CBUUID`](cbuuid.md) objects that identify a peripheral’s services, characteristics, and descriptors.

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbpeer/identifier)*