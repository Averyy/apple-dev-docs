# linkedCoreAudioDeviceUID

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A universal identifier of the audio device linked to this device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var linkedCoreAudioDeviceUID: String? { get set }
```

```objc
@property (atomic, strong, nullable) NSString * linkedCoreAudioDeviceUID;
```

#### Discussion

The key for this property is [`deviceLinkedCoreAudioDeviceUID`](../cmioextensionproperty/devicelinkedcoreaudiodeviceuid.md).

## See Also

### Configuring Device Properties
- [var model: String?](./model.md)
  A device model string.
- [var transportType: Int?](./transporttype-96gm.md)
  The transport type of the device, such as USB or HDMI.
- [var suspended: Bool?](./suspended-eru0.md)
  A Boolean value that indicates whether the device is in a suspended state.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](./setpropertystate%28_,forproperty%29.md)
  Sets the value of a device property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./propertiesdictionary.md)
  A dictionary of properties for a device.
- [transportType](./transporttype-25qzh.md)
  The transport type of the device, such as USB or HDMI.
- [suspended](./suspended-2ja7h.md)
  A Boolean value that indicates whether the device is in a suspended state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/linkedcoreaudiodeviceuid)*