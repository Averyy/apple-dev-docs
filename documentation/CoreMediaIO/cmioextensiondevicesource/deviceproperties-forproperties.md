# deviceProperties(forProperties:)

**Framework**: Core Media I/O  
**Kind**: method  
**Required**: Yes

Retrieves the state of device properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func deviceProperties(forProperties properties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionDeviceProperties
```

#### Return Value

A properties object that contains the current device state.

## Parameters

- `properties`: A set of device properties to retrieve.

## See Also

- [var availableProperties: Set<CMIOExtensionProperty>](cmioextensiondevicesource/availableproperties.md)
  A set of available properties that a device provides.
- [func setDeviceProperties(CMIOExtensionDeviceProperties) throws](cmioextensiondevicesource/setdeviceproperties(_:).md)
  Sets the state of device properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevicesource/deviceproperties(forproperties:))*