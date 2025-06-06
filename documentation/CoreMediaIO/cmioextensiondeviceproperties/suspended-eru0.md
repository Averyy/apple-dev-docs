# suspended

**Framework**: Core Media I/O  
**Kind**: property

A Boolean value that indicates whether the device is in a suspended state.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+
- Xcode 13.0+

## Declaration

```swift
@nonobjc
var suspended: Bool? { get set }
```

#### Discussion

The key for this property is [`deviceIsSuspended`](cmioextensionproperty/deviceissuspended.md).

## See Also

- [var model: String?](cmioextensiondeviceproperties/model.md)
  A device model string.
- [var linkedCoreAudioDeviceUID: String?](cmioextensiondeviceproperties/linkedcoreaudiodeviceuid.md)
  A universal identifier of the audio device linked to this device.
- [var transportType: Int?](cmioextensiondeviceproperties/transporttype-96gm.md)
  The transport type of the device, such as USB or HDMI.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](cmioextensiondeviceproperties/setpropertystate(_:forproperty:).md)
  Sets the value of a device property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](cmioextensiondeviceproperties/propertiesdictionary.md)
  A dictionary of properties for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/suspended-eru0)*