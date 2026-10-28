# GetDeviceIsAlive

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets a Boolean value that represents whether the device is alive.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
bool GetDeviceIsAlive();
```

## Return Value

`true` if the device is alive; `false` otherwise.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Clock Device State
- [GetDeviceIsRunning](./getdeviceisrunning.md)
  Gets a Boolean value that indicates whether the device is running.
- [SetDeviceIsAlive](./setdeviceisalive.md)
  Sets a Boolean value to represent whether the device is alive.
- [SetIsHidden](./setishidden.md)
  Sets a Boolean value to indicate whether the device is hidden.
- [GetIsHidden](./getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getdeviceisalive)*