# deviceTransportType

**Framework**: Core Media I/O  
**Kind**: property

A property key for the device transport type.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static let deviceTransportType: CMIOExtensionProperty
```

#### Discussion

The property state for this property is a number value that corresponds to an audio transport type (`kIOAudioDeviceTransportType`) that the IOKit framework defines.

## See Also

- [static let deviceModel: CMIOExtensionProperty](cmioextensionproperty/devicemodel.md)
  A property key for the device model.
- [static let deviceIsSuspended: CMIOExtensionProperty](cmioextensionproperty/deviceissuspended.md)
  A property key for a Boolean value that indicates whether the device is in a suspended state.
- [static let deviceLinkedCoreAudioDeviceUID: CMIOExtensionProperty](cmioextensionproperty/devicelinkedcoreaudiodeviceuid.md)
  A property key for the UID of the linked Core Audio device.
- [static let deviceCanBeDefaultInputDevice: CMIOExtensionProperty](cmioextensionproperty/devicecanbedefaultinputdevice.md)
  A property key for a Boolean value that indicates whether the device can be a default input device.
- [static let deviceCanBeDefaultOutputDevice: CMIOExtensionProperty](cmioextensionproperty/devicecanbedefaultoutputdevice.md)
  A property key for a Boolean value that indicates whether the device can be a default output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty/devicetransporttype)*