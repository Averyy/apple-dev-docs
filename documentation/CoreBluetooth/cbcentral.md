# CBCentral

**Framework**: Core Bluetooth  
**Kind**: class

A remote device connected to a local app, which is acting as a peripheral.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CBCentral
```

#### Overview

The [`CBCentral`](cbcentral.md) class represents remote central devices (or *centrals*) that have connected to an app implementing the peripheral role on a local device. Remote centrals use universally unique identifiers (UUIDs), represented by [`NSUUID`](https://developer.apple.com/documentation/foundation/nsuuid) objects, to identify themselves.

## Topics

### Identifying a Remote Central
- [var maximumUpdateValueLength: Int](cbcentral/maximumupdatevaluelength.md)
  The maximum amount of data, in bytes, that the central can receive in a single notification or indication.

## Relationships

### Inherits From
- [CBPeer](cbpeer.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class CBCentralManager](cbcentralmanager.md)
  An object that scans for, discovers, connects to, and manages peripherals.
- [protocol CBCentralManagerDelegate](cbcentralmanagerdelegate.md)
  A protocol that provides updates for the discovery and management of peripheral devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentral)*