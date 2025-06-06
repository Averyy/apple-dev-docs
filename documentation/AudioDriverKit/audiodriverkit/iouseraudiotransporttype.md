# IOUserAudioTransportType

**Framework**: AudioDriverKit  
**Kind**: enum

The type of transport to deliver audio.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioTransportType : uint32_t;
```

## Topics

### Protocol-based Transport Types
- [PCI](audiodriverkit/iouseraudiotransporttype/pci.md)
  The transport type ID for audio devices connected with the PCI bus.
- [USB](audiodriverkit/iouseraudiotransporttype/usb.md)
  The transport type ID for audio devices connected with USB.
- [FireWire](audiodriverkit/iouseraudiotransporttype/firewire.md)
  The transport type ID for audio devices connected with FireWire.
- [Bluetooth](audiodriverkit/iouseraudiotransporttype/bluetooth.md)
  The transport type ID for audio devices connected with Bluetooth.
- [BluetoothLE](audiodriverkit/iouseraudiotransporttype/bluetoothle.md)
  The transport type ID for audio devices connected with Bluetooth Low Energy.
- [HDMI](audiodriverkit/iouseraudiotransporttype/hdmi.md)
  The transport type ID for audio devices connected with HDMI.
- [DisplayPort](audiodriverkit/iouseraudiotransporttype/displayport.md)
  The transport type ID for audio devices connected with DisplayPort.
- [AirPlay](audiodriverkit/iouseraudiotransporttype/airplay.md)
  The transport type ID for audio devices connected with AirPlay.
- [AVB](audiodriverkit/iouseraudiotransporttype/avb.md)
  The transport type ID for audio devices connected with Audio Video Bridging (AVB).
- [Thunderbolt](audiodriverkit/iouseraudiotransporttype/thunderbolt.md)
  The transport type ID for audio devices connected with Thunderbolt.
### Other Transport Types
- [Unknown](audiodriverkit/iouseraudiotransporttype/unknown.md)
  The transport type ID returned when a device doesn’t provide a transport type.
- [BuiltIn](audiodriverkit/iouseraudiotransporttype/builtin.md)
  The transport type ID for AudioDevices built into the system.

## See Also

- [SetTransportType](iouseraudiobox/settransporttype.md)
  Sets the box’s transport type.
- [GetTransportType](iouseraudiobox/gettransporttype.md)
  Returns the box’s transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiotransporttype)*