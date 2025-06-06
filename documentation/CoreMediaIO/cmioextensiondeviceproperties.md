# CMIOExtensionDeviceProperties

**Framework**: Core Media I/O  
**Kind**: class

An object that defines the properties of a device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionDeviceProperties
```

#### Overview

Create an instance of this object to manage the device’s property state.

## Topics

### Creating Device Properties
- [init(dictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](cmioextensiondeviceproperties/init(dictionary:).md)
  Creates a properties object with a dictionary of property states.
### Configuring Device Properties
- [var model: String?](cmioextensiondeviceproperties/model.md)
  A device model string.
- [var linkedCoreAudioDeviceUID: String?](cmioextensiondeviceproperties/linkedcoreaudiodeviceuid.md)
  A universal identifier of the audio device linked to this device.
- [var transportType: Int?](cmioextensiondeviceproperties/transporttype-96gm.md)
  The transport type of the device, such as USB or HDMI.
- [var suspended: Bool?](cmioextensiondeviceproperties/suspended-eru0.md)
  A Boolean value that indicates whether the device is in a suspended state.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](cmioextensiondeviceproperties/setpropertystate(_:forproperty:).md)
  Sets the value of a device property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](cmioextensiondeviceproperties/propertiesdictionary.md)
  A dictionary of properties for a device.

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

- [class CMIOExtensionDevice](cmioextensiondevice.md)
  An object that represents a physical or virtual device.
- [protocol CMIOExtensionDeviceSource](cmioextensiondevicesource.md)
  A protocol for objects that act as device sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties)*