# propertiesDictionary

**Framework**: Core Media I/O  
**Kind**: property

A dictionary of properties for a device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>] { get set }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/propertiesdictionary)*