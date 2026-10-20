# deviceCanBeDefaultOutputDevice

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Type Property

A property key for a Boolean value that indicates whether the device can be a default output device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static let deviceCanBeDefaultOutputDevice: CMIOExtensionProperty
```

```c
extern CMIOExtensionProperty const CMIOExtensionPropertyDeviceCanBeDefaultOutputDevice;
```

#### Discussion

The property state for this property is a number that represents a Boolean value.

## See Also

### Device Properties
- [static let deviceModel: CMIOExtensionProperty](./devicemodel.md)
  A property key for the device model.
- [static let deviceIsSuspended: CMIOExtensionProperty](./deviceissuspended.md)
  A property key for a Boolean value that indicates whether the device is in a suspended state.
- [static let deviceTransportType: CMIOExtensionProperty](./devicetransporttype.md)
  A property key for the device transport type.
- [static let deviceLinkedCoreAudioDeviceUID: CMIOExtensionProperty](./devicelinkedcoreaudiodeviceuid.md)
  A property key for the UID of the linked Core Audio device.
- [static let deviceCanBeDefaultInputDevice: CMIOExtensionProperty](./devicecanbedefaultinputdevice.md)
  A property key for a Boolean value that indicates whether the device can be a default input device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty/devicecanbedefaultoutputdevice)*