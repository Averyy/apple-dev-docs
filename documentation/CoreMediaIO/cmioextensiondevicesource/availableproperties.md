# availableProperties

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A set of available properties that a device provides.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var availableProperties: Set<CMIOExtensionProperty> { get }
```

```objc
@property (atomic, copy, readonly) NSSet<NSString *> * availableProperties;
```

#### Discussion

Don’t change the state of this property during the life cycle of the associated device.

## See Also

### Managing Properties
- [func deviceProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionDeviceProperties](./deviceproperties%28forproperties%29.md)
  Retrieves the state of device properties.
- [func setDeviceProperties(CMIOExtensionDeviceProperties) throws](./setdeviceproperties%28_%29.md)
  Sets the state of device properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevicesource/availableproperties)*