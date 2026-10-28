# suspended

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device is in a suspended state.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
@property (atomic, strong, nullable) NSNumber * suspended;
```

## Discussion

The key for this property is [`deviceIsSuspended`](../cmioextensionproperty/deviceissuspended.md).

## See Also

### Configuring Device Properties
- [var model: String?](./model.md)
  A device model string.
- [var linkedCoreAudioDeviceUID: String?](./linkedcoreaudiodeviceuid.md)
  A universal identifier of the audio device linked to this device.
- [transportType](./transporttype-25qzh.md)
  The transport type of the device, such as USB or HDMI.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](./setpropertystate%28_,forproperty%29.md)
  Sets the value of a device property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./propertiesdictionary.md)
  A dictionary of properties for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/suspended-2ja7h)*