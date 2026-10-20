# CBCentral

**Framework**: Core Bluetooth  
**Kind**: class  
**Role**: Class

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

```objc
@interface CBCentral : CBPeer
```

#### Overview

The [`CBCentral`](./cbcentral.md) class represents remote central devices (or *centrals*) that have connected to an app implementing the peripheral role on a local device. Remote centrals use universally unique identifiers (UUIDs), represented by [`NSUUID`](../Foundation/nsuuid.md) objects, to identify themselves.

## Topics

### Identifying a Remote Central
- [var maximumUpdateValueLength: Int](./cbcentral/maximumupdatevaluelength.md)
  The maximum amount of data, in bytes, that the central can receive in a single notification or indication.

## Relationships

### Inherits From
- [CBPeer](./cbpeer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Centrals
- [class CBCentralManager](./cbcentralmanager.md)
  An object that scans for, discovers, connects to, and manages peripherals.
- [protocol CBCentralManagerDelegate](./cbcentralmanagerdelegate.md)
  A protocol that provides updates for the discovery and management of peripheral devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentral)*