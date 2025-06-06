# deviceIsSuspended

**Framework**: Core Media I/O  
**Kind**: property

A property key for a Boolean value that indicates whether the device is in a suspended state.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
static let deviceIsSuspended: CMIOExtensionProperty
```

#### Discussion

An example of when a device may be in a suspended state is when a user closes their laptop. While suspended, the device continues to respond to requests as if it were active, but the stream doesn’t provide any data.

The property state for this property is a number that represents a Boolean value.

## See Also

- [static let deviceModel: CMIOExtensionProperty](cmioextensionproperty/devicemodel.md)
  A property key for the device model.
- [static let deviceTransportType: CMIOExtensionProperty](cmioextensionproperty/devicetransporttype.md)
  A property key for the device transport type.
- [static let deviceLinkedCoreAudioDeviceUID: CMIOExtensionProperty](cmioextensionproperty/devicelinkedcoreaudiodeviceuid.md)
  A property key for the UID of the linked Core Audio device.
- [static let deviceCanBeDefaultInputDevice: CMIOExtensionProperty](cmioextensionproperty/devicecanbedefaultinputdevice.md)
  A property key for a Boolean value that indicates whether the device can be a default input device.
- [static let deviceCanBeDefaultOutputDevice: CMIOExtensionProperty](cmioextensionproperty/devicecanbedefaultoutputdevice.md)
  A property key for a Boolean value that indicates whether the device can be a default output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty/deviceissuspended)*