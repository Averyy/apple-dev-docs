# availableProperties

**Framework**: Core Media I/O  
**Kind**: property  
**Required**: Yes

A set of available properties that a device provides.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var availableProperties: Set<CMIOExtensionProperty> { get }
```

#### Discussion

Don’t change the state of this property during the life cycle of the associated device.

## See Also

- [func deviceProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionDeviceProperties](cmioextensiondevicesource/deviceproperties(forproperties:).md)
  Retrieves the state of device properties.
- [func setDeviceProperties(CMIOExtensionDeviceProperties) throws](cmioextensiondevicesource/setdeviceproperties(_:).md)
  Sets the state of device properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevicesource/availableproperties)*