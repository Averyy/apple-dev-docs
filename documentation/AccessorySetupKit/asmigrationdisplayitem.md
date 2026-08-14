# ASMigrationDisplayItem

**Framework**: AccessorySetupKit  
**Kind**: class

A previously-discovered accessory as presented by the discovery picker, for use when migrating it to AccessorySetupKit.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASMigrationDisplayItem
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Overview

Create instances of `ASMigrationDisplayItem` by calling the superclass’s initializer [`init(name:productImage:descriptor:)`](aspickerdisplayitem/init(name:productimage:descriptor:).md), then specify the Bluetooth [`peripheralIdentifier`](asmigrationdisplayitem/peripheralidentifier.md), the Wi-Fi [`hotspotSSID`](asmigrationdisplayitem/hotspotssid.md), or both, for the specific accessory you want to migrate.

## Topics

### Accessory identifiers
- [var peripheralIdentifier: UUID?](asmigrationdisplayitem/peripheralidentifier.md)
  The Bluetooth identifier of the accessory to migrate.
- [var hotspotSSID: String?](asmigrationdisplayitem/hotspotssid.md)
  The Wi-Fi hotspot SSID of the accessory to migrate.
- [var wifiAwarePairedDeviceID: ASAccessory.WiFiAwarePairedDeviceID](asmigrationdisplayitem/wifiawarepaireddeviceid.md)
  The Wi-Fi Aware paired device identififer of the accessory to migrate.

## Relationships

### Inherits From
- [ASPickerDisplayItem](aspickerdisplayitem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class ASPickerDisplayItem](aspickerdisplayitem.md)
  An accessory as presented by the discovery picker.
- [class ASDiscoveredDisplayItem](asdiscovereddisplayitem.md)
  A picker display item created from customizing a discovered accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asmigrationdisplayitem)*