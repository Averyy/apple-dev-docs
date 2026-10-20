# CanBeDefaultSystemOutputDevice

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if this device can be the system’s default output device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
uint32_t CanBeDefaultSystemOutputDevice();
```

#### Return Value

`true` if the system can use this device as the default output device.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Default Device Behavior
- [SetCanBeDefaultInputDevice](./setcanbedefaultinputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default input device.
- [CanBeDefaultInputDevice](./canbedefaultinputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default input device.
- [SetCanBeDefaultOutputDevice](./setcanbedefaultoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default output device.
- [CanBeDefaultOutputDevice](./canbedefaultoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default output device.
- [SetCanBeDefaultSystemOutputDevice](./setcanbedefaultsystemoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the system’s default output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/canbedefaultsystemoutputdevice)*