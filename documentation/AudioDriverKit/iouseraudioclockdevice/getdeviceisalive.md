# GetDeviceIsAlive

**Framework**: AudioDriverKit  
**Kind**: method

Gets a Boolean value that represents whether the device is alive.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool GetDeviceIsAlive();
```

#### Return Value

`true` if the device is alive; `false` otherwise.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [GetDeviceIsRunning](iouseraudioclockdevice/getdeviceisrunning.md)
  Gets a Boolean value that indicates whether the device is running.
- [SetDeviceIsAlive](iouseraudioclockdevice/setdeviceisalive.md)
  Sets a Boolean value to represent whether the device is alive.
- [SetIsHidden](iouseraudioclockdevice/setishidden.md)
  Sets a Boolean value to indicate whether the device is hidden.
- [GetIsHidden](iouseraudioclockdevice/getishidden.md)
  Gets a Boolean value that indicates whether the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getdeviceisalive)*