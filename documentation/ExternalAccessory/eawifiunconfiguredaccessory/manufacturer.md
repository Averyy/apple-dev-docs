# manufacturer

**Framework**: External Accessory  
**Kind**: property  
**Role**: Instance Property

The name of the accessory’s manufacturer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var manufacturer: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * manufacturer;
```

## See Also

### Getting Information About the Accessory
- [var name: String](./name.md)
  The name of the accessory.
- [var model: String](./model.md)
  The model name of accessory.
- [var ssid: String](./ssid.md)
  The Wi-Fi SSID of the accessory.
- [var macAddress: String](./macaddress.md)
  The primary MAC address of the accessory.
- [var properties: EAWiFiUnconfiguredAccessoryProperties](./properties.md)
  The properties the accessory supports.
- [struct EAWiFiUnconfiguredAccessoryProperties](../eawifiunconfiguredaccessoryproperties.md)
  Options that can be combined using the C bitwise `OR` operator to represent the properties of an unconfigured accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/manufacturer)*