# SetCanBeDefaultInputDevice

**Framework**: AudioDriverKit  
**Kind**: method

Sets a Boolean value that indicates if this device can be the host’s default input device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetCanBeDefaultInputDevice(bool in_can_be_default);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_can_be_default`:   if the host can use this device as the default input device.

## See Also

- [CanBeDefaultInputDevice](iouseraudiodevice/canbedefaultinputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default input device.
- [SetCanBeDefaultOutputDevice](iouseraudiodevice/setcanbedefaultoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default output device.
- [CanBeDefaultOutputDevice](iouseraudiodevice/canbedefaultoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default output device.
- [SetCanBeDefaultSystemOutputDevice](iouseraudiodevice/setcanbedefaultsystemoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the system’s default output device.
- [CanBeDefaultSystemOutputDevice](iouseraudiodevice/canbedefaultsystemoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the system’s default output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setcanbedefaultinputdevice)*