# SetIsHidden

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value to indicate whether the device is hidden.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetIsHidden(bool in_is_hidden);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

A true value indicates the device isn’t included in the normal list of devices, and is only findable by its UID. A hidden device can’t be the default device.

## Parameters

- `in_is_hidden`: `true` if the device is hidden; otherwise, `false`.

## See Also

### Working with Clock Device State
- [GetDeviceIsRunning](./getdeviceisrunning.md)
  Gets a Boolean value that indicates whether the device is running.
- [SetDeviceIsAlive](./setdeviceisalive.md)
  Sets a Boolean value to represent whether the device is alive.
- [GetDeviceIsAlive](./getdeviceisalive.md)
  Gets a Boolean value that represents whether the device is alive.
- [GetIsHidden](./getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setishidden)*