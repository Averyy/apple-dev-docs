# EAWiFiUnconfiguredAccessoryProperties

**Framework**: External Accessory  
**Kind**: struct

Options that can be combined using the C bitwise `OR` operator to represent the properties of an unconfigured accessory.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct EAWiFiUnconfiguredAccessoryProperties
```

## Topics

### Getting the Accessory Properties
- [static var propertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties](eawifiunconfiguredaccessoryproperties/propertysupportsairplay.md)
  The accessory indicates that it supports AirPlay.
- [static var propertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties](eawifiunconfiguredaccessoryproperties/propertysupportsairprint.md)
  The accessory indicates that it supports AirPrint.
- [static var propertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties](eawifiunconfiguredaccessoryproperties/propertysupportshomekit.md)
  The accessory indicates that it supports HomeKit.
### Initializers
- [init(rawValue: UInt)](eawifiunconfiguredaccessoryproperties/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var name: String](eawifiunconfiguredaccessory/name.md)
  The name of the accessory.
- [var manufacturer: String](eawifiunconfiguredaccessory/manufacturer.md)
  The name of the accessory’s manufacturer.
- [var model: String](eawifiunconfiguredaccessory/model.md)
  The model name of accessory.
- [var ssid: String](eawifiunconfiguredaccessory/ssid.md)
  The Wi-Fi SSID of the accessory.
- [var macAddress: String](eawifiunconfiguredaccessory/macaddress.md)
  The primary MAC address of the accessory.
- [var properties: EAWiFiUnconfiguredAccessoryProperties](eawifiunconfiguredaccessory/properties.md)
  The properties the accessory supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties)*