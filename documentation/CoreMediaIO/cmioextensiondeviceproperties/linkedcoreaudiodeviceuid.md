# linkedCoreAudioDeviceUID

**Framework**: Core Media I/O  
**Kind**: property

A universal identifier of the audio device linked to this device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var linkedCoreAudioDeviceUID: String? { get set }
```

#### Discussion

The key for this property is [`deviceLinkedCoreAudioDeviceUID`](cmioextensionproperty/devicelinkedcoreaudiodeviceuid.md).

## See Also

- [var model: String?](cmioextensiondeviceproperties/model.md)
  A device model string.
- [var transportType: Int?](cmioextensiondeviceproperties/transporttype-96gm.md)
  The transport type of the device, such as USB or HDMI.
- [var suspended: Bool?](cmioextensiondeviceproperties/suspended-eru0.md)
  A Boolean value that indicates whether the device is in a suspended state.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](cmioextensiondeviceproperties/setpropertystate(_:forproperty:).md)
  Sets the value of a device property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](cmioextensiondeviceproperties/propertiesdictionary.md)
  A dictionary of properties for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/linkedcoreaudiodeviceuid)*