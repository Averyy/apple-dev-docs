# SetIsHidden

**Framework**: AudioDriverKit  
**Kind**: method

Sets a Boolean value to indicate whether the device is hidden.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetIsHidden(bool in_is_hidden);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

A true value indicates the device isn’t included in the normal list of devices, and is only findable by its UID. A hidden device can’t be the default device.

## Parameters

- `in_is_hidden`:   if the device is hidden; otherwise,  .

## See Also

- [GetDeviceIsRunning](iouseraudioclockdevice/getdeviceisrunning.md)
  Gets a Boolean value that indicates whether the device is running.
- [SetDeviceIsAlive](iouseraudioclockdevice/setdeviceisalive.md)
  Sets a Boolean value to represent whether the device is alive.
- [GetDeviceIsAlive](iouseraudioclockdevice/getdeviceisalive.md)
  Gets a Boolean value that represents whether the device is alive.
- [GetIsHidden](iouseraudioclockdevice/getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setishidden)*