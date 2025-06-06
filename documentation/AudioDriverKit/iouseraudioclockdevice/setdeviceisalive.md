# SetDeviceIsAlive

**Framework**: AudioDriverKit  
**Kind**: method

Sets a Boolean value to represent whether the device is alive.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetDeviceIsAlive(bool in_is_alive);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

A `true` value means the device is ready and available. `false` means the device is unusable and will most likely go away shortly.

## Parameters

- `in_is_alive`:   if the device is alive; otherwise,  .

## See Also

- [GetDeviceIsRunning](iouseraudioclockdevice/getdeviceisrunning.md)
  Gets a Boolean value that indicates whether the device is running.
- [GetDeviceIsAlive](iouseraudioclockdevice/getdeviceisalive.md)
  Gets a Boolean value that represents whether the device is alive.
- [SetIsHidden](iouseraudioclockdevice/setishidden.md)
  Sets a Boolean value to indicate whether the device is hidden.
- [GetIsHidden](iouseraudioclockdevice/getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setdeviceisalive)*