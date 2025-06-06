# CMIOExtensionProperty

**Framework**: Core Media I/O  
**Kind**: struct

A structure that defines the properties that providers, devices, and streams support.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
struct CMIOExtensionProperty
```

## Topics

### Provider Properties
- [static let providerName: CMIOExtensionProperty](cmioextensionproperty/providername.md)
  A property key for the provider name.
- [static let providerManufacturer: CMIOExtensionProperty](cmioextensionproperty/providermanufacturer.md)
  A property key for the provider manufacturer.
### Device Properties
- [static let deviceModel: CMIOExtensionProperty](cmioextensionproperty/devicemodel.md)
  A property key for the device model.
- [static let deviceIsSuspended: CMIOExtensionProperty](cmioextensionproperty/deviceissuspended.md)
  A property key for a Boolean value that indicates whether the device is in a suspended state.
- [static let deviceTransportType: CMIOExtensionProperty](cmioextensionproperty/devicetransporttype.md)
  A property key for the device transport type.
- [static let deviceLinkedCoreAudioDeviceUID: CMIOExtensionProperty](cmioextensionproperty/devicelinkedcoreaudiodeviceuid.md)
  A property key for the UID of the linked Core Audio device.
- [static let deviceCanBeDefaultInputDevice: CMIOExtensionProperty](cmioextensionproperty/devicecanbedefaultinputdevice.md)
  A property key for a Boolean value that indicates whether the device can be a default input device.
- [static let deviceCanBeDefaultOutputDevice: CMIOExtensionProperty](cmioextensionproperty/devicecanbedefaultoutputdevice.md)
  A property key for a Boolean value that indicates whether the device can be a default output device.
### Stream Properties
- [static let streamActiveFormatIndex: CMIOExtensionProperty](cmioextensionproperty/streamactiveformatindex.md)
  A property key for the index of the active stream format.
- [static let streamFrameDuration: CMIOExtensionProperty](cmioextensionproperty/streamframeduration.md)
  A property key for the frame duration.
- [static let streamMaxFrameDuration: CMIOExtensionProperty](cmioextensionproperty/streammaxframeduration.md)
  A property key for the maximum frame duration.
- [static let streamSinkBufferQueueSize: CMIOExtensionProperty](cmioextensionproperty/streamsinkbufferqueuesize.md)
  A property key for the sink buffer queue size.
- [static let streamSinkBuffersRequiredForStartup: CMIOExtensionProperty](cmioextensionproperty/streamsinkbuffersrequiredforstartup.md)
  A property key for the number of buffers required for startup.
- [static let streamSinkBufferUnderrunCount: CMIOExtensionProperty](cmioextensionproperty/streamsinkbufferunderruncount.md)
  A property key for the buffer underrun count.
- [static let streamSinkEndOfData: CMIOExtensionProperty](cmioextensionproperty/streamsinkendofdata.md)
  A property key for a Boolean value that indicates whether the stream has more data.
### Type Properties
- [static let deviceLatency: CMIOExtensionProperty](cmioextensionproperty/devicelatency.md)
- [static let streamLatency: CMIOExtensionProperty](cmioextensionproperty/streamlatency.md)
- [init(rawValue: String)](cmioextensionproperty/init(rawvalue:).md)
  Creates a property with a raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CMIOExtensionPropertyState](cmioextensionpropertystate.md)
  An object that describes the state of a property.
- [class CMIOExtensionPropertyAttributes](cmioextensionpropertyattributes.md)
  An object that describes the attributes of a property.
- [let CMIOExtensionInfoDictionaryKey: String](cmioextensioninfodictionarykey.md)
  A key that specifies the extension information dictionary.
- [let CMIOExtensionMachServiceNameKey: String](cmioextensionmachservicenamekey.md)
  A key that specifies the mach service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty)*