# ASDiscoveredAccessory

**Framework**: AccessorySetupKit  
**Kind**: class

A discovered accessory, for use in creating a customized picker display item.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
class ASDiscoveredAccessory
```

#### Overview

When your app’s picker uses the [`filterDiscoveryResults`](aspickerdisplaysettings/options-swift.struct/filterdiscoveryresults.md) option, you receive [`ASAccessoryEventType.accessoryDiscovered`](asaccessoryeventtype/accessorydiscovered.md) events that contain this type. Use the discovered accessory’s Bluetooth properties to create a new [`ASDiscoveredDisplayItem`](asdiscovereddisplayitem.md), incorporating traits like a custom accessory name or a newly downloaded product image. You can then add this item to the picker to allow the person using the app to set up the accessory.

## Topics

### Working with accessory properties
- [var bluetoothAdvertisementData: [AnyHashable : Any]?](asdiscoveredaccessory/bluetoothadvertisementdata.md)
  The Bluetooth advertisement data from the discovered accessory.
- [var bluetoothRSSI: Int?](asdiscoveredaccessory/bluetoothrssi-5a2gp.md)
  The Bluetooth RSSI (Received Signal Strength Indicator) value from the discovered accessory.

## Relationships

### Inherits From
- [ASAccessory](asaccessory.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ASAccessory](asaccessory.md)
  An accessory discovered by the accessory session.
- [ASAccessory.AccessoryState](asaccessory/accessorystate.md)
  An enumeration of possible authorization states of an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscoveredaccessory)*