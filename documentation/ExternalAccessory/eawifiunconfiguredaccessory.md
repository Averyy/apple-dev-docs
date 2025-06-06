# EAWiFiUnconfiguredAccessory

**Framework**: External Accessory  
**Kind**: class

An object that provides information about an unconfigured MFi Wireless Accessory Configuration accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class EAWiFiUnconfiguredAccessory
```

## Topics

### Getting Information About the Accessory
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
- [struct EAWiFiUnconfiguredAccessoryProperties](eawifiunconfiguredaccessoryproperties.md)
  Options that can be combined using the C bitwise `OR` operator to represent the properties of an unconfigured accessory.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Wireless Accessory Configuration Entitlement](../BundleResources/Entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [class EAWiFiUnconfiguredAccessoryBrowser](eawifiunconfiguredaccessorybrowser.md)
  An object you use to scan for wireless accessories and configure them for use with the user’s app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory)*