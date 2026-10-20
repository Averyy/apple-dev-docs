# SetDeviceIsAlive

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value to represent whether the device is alive.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetDeviceIsAlive(bool in_is_alive);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

A `true` value means the device is ready and available. `false` means the device is unusable and will most likely go away shortly.

## Parameters

- `in_is_alive`: `true` if the device is alive; otherwise, `false`.

## See Also

### Working with Clock Device State
- [GetDeviceIsRunning](./getdeviceisrunning.md)
  Gets a Boolean value that indicates whether the device is running.
- [GetDeviceIsAlive](./getdeviceisalive.md)
  Gets a Boolean value that represents whether the device is alive.
- [SetIsHidden](./setishidden.md)
  Sets a Boolean value to indicate whether the device is hidden.
- [GetIsHidden](./getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setdeviceisalive)*