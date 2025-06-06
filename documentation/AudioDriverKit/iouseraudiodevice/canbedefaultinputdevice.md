# CanBeDefaultInputDevice

**Framework**: AudioDriverKit  
**Kind**: method

Returns a Boolean value that indicates if this device can be the host’s default input device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t CanBeDefaultInputDevice();
```

#### Return Value

`true` if the host can use this device as the default input device.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetCanBeDefaultInputDevice](iouseraudiodevice/setcanbedefaultinputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default input device.
- [SetCanBeDefaultOutputDevice](iouseraudiodevice/setcanbedefaultoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default output device.
- [CanBeDefaultOutputDevice](iouseraudiodevice/canbedefaultoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default output device.
- [SetCanBeDefaultSystemOutputDevice](iouseraudiodevice/setcanbedefaultsystemoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the system’s default output device.
- [CanBeDefaultSystemOutputDevice](iouseraudiodevice/canbedefaultsystemoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the system’s default output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/canbedefaultinputdevice)*