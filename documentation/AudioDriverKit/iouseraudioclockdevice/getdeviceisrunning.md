# GetDeviceIsRunning

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets a Boolean value that indicates whether the device is running.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
bool GetDeviceIsRunning();
```

## Return Value

`true` if the device is running; `false` otherwise.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Clock Device State
- [SetDeviceIsAlive](./setdeviceisalive.md)
  Sets a Boolean value to represent whether the device is alive.
- [GetDeviceIsAlive](./getdeviceisalive.md)
  Gets a Boolean value that represents whether the device is alive.
- [SetIsHidden](./setishidden.md)
  Sets a Boolean value to indicate whether the device is hidden.
- [GetIsHidden](./getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getdeviceisrunning)*