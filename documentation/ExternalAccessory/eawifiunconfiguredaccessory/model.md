# model

**Framework**: External Accessory  
**Kind**: property  
**Role**: Instance Property

The model name of accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var model: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * model;
```

## See Also

### Getting Information About the Accessory
- [var name: String](./name.md)
  The name of the accessory.
- [var manufacturer: String](./manufacturer.md)
  The name of the accessory’s manufacturer.
- [var ssid: String](./ssid.md)
  The Wi-Fi SSID of the accessory.
- [var macAddress: String](./macaddress.md)
  The primary MAC address of the accessory.
- [var properties: EAWiFiUnconfiguredAccessoryProperties](./properties.md)
  The properties the accessory supports.
- [struct EAWiFiUnconfiguredAccessoryProperties](../eawifiunconfiguredaccessoryproperties.md)
  Options that can be combined using the C bitwise `OR` operator to represent the properties of an unconfigured accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/model)*