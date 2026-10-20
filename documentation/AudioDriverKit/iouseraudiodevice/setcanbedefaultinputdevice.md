# SetCanBeDefaultInputDevice

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value that indicates if this device can be the host’s default input device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetCanBeDefaultInputDevice(bool in_can_be_default);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_can_be_default`: `true` if the host can use this device as the default input device.

## See Also

### Working with Default Device Behavior
- [CanBeDefaultInputDevice](./canbedefaultinputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default input device.
- [SetCanBeDefaultOutputDevice](./setcanbedefaultoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the host’s default output device.
- [CanBeDefaultOutputDevice](./canbedefaultoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the host’s default output device.
- [SetCanBeDefaultSystemOutputDevice](./setcanbedefaultsystemoutputdevice.md)
  Sets a Boolean value that indicates if this device can be the system’s default output device.
- [CanBeDefaultSystemOutputDevice](./canbedefaultsystemoutputdevice.md)
  Returns a Boolean value that indicates if this device can be the system’s default output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setcanbedefaultinputdevice)*