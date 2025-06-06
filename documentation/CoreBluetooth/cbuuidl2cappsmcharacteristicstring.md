# CBUUIDL2CAPPSMCharacteristicString

**Framework**: Core Bluetooth  
**Kind**: var

The PSM of an L2CAP channel associated with the GATT service containing this characteristic.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let CBUUIDL2CAPPSMCharacteristicString: String
```

#### Discussion

This PSM is a little-endian [`UInt16`](https://developer.apple.com/documentation/Swift/UInt16). Servers can publish this characteristic with the UUID `ABDD3056-28FA-441D-A470-55A75A52553A`.

## See Also

- [let CBUUIDCharacteristicExtendedPropertiesString: String](cbuuidcharacteristicextendedpropertiesstring.md)
  The UUID for the Extended Properties descriptor, as a string.
- [let CBUUIDCharacteristicUserDescriptionString: String](cbuuidcharacteristicuserdescriptionstring.md)
  The UUID for the User Description descriptor, as a string.
- [let CBUUIDClientCharacteristicConfigurationString: String](cbuuidclientcharacteristicconfigurationstring.md)
  The UUID for the Client Configuration descriptor, as a string.
- [let CBUUIDServerCharacteristicConfigurationString: String](cbuuidservercharacteristicconfigurationstring.md)
  The UUID for the Server Configuration descriptor, as a string.
- [let CBUUIDCharacteristicFormatString: String](cbuuidcharacteristicformatstring.md)
  The UUID for the Presentation Format descriptor, as a string.
- [let CBUUIDCharacteristicAggregateFormatString: String](cbuuidcharacteristicaggregateformatstring.md)
  The UUID for the Aggregate Format descriptor, as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuidl2cappsmcharacteristicstring)*