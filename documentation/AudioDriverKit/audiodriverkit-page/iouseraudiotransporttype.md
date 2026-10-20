# IOUserAudioTransportType

**Framework**: AudioDriverKit  
**Kind**: enum  
**Role**: Enumeration

The type of transport to deliver audio.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
enum IOUserAudioTransportType : uint32_t;
```

## Topics

### Protocol-based Transport Types
- [PCI](./iouseraudiotransporttype/pci.md)
  The transport type ID for audio devices connected with the PCI bus.
- [USB](./iouseraudiotransporttype/usb.md)
  The transport type ID for audio devices connected with USB.
- [FireWire](./iouseraudiotransporttype/firewire.md)
  The transport type ID for audio devices connected with FireWire.
- [Bluetooth](./iouseraudiotransporttype/bluetooth.md)
  The transport type ID for audio devices connected with Bluetooth.
- [BluetoothLE](./iouseraudiotransporttype/bluetoothle.md)
  The transport type ID for audio devices connected with Bluetooth Low Energy.
- [HDMI](./iouseraudiotransporttype/hdmi.md)
  The transport type ID for audio devices connected with HDMI.
- [DisplayPort](./iouseraudiotransporttype/displayport.md)
  The transport type ID for audio devices connected with DisplayPort.
- [AirPlay](./iouseraudiotransporttype/airplay.md)
  The transport type ID for audio devices connected with AirPlay.
- [AVB](./iouseraudiotransporttype/avb.md)
  The transport type ID for audio devices connected with Audio Video Bridging (AVB).
- [Thunderbolt](./iouseraudiotransporttype/thunderbolt.md)
  The transport type ID for audio devices connected with Thunderbolt.
### Other Transport Types
- [Unknown](./iouseraudiotransporttype/unknown.md)
  The transport type ID returned when a device doesn’t provide a transport type.
- [BuiltIn](./iouseraudiotransporttype/builtin.md)
  The transport type ID for AudioDevices built into the system.

## See Also

### Working with Transport Types
- [SetTransportType](../iouseraudiobox/settransporttype.md)
  Sets the box’s transport type.
- [GetTransportType](../iouseraudiobox/gettransporttype.md)
  Returns the box’s transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiotransporttype)*