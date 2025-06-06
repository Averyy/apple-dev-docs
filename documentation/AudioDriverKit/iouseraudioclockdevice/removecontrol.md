# RemoveControl

**Framework**: AudioDriverKit  
**Kind**: method

Removes a control from the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t RemoveControl(IOUserAudioControl * in_control);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If removing the control succeeds, the control’s reference count decrements by one.

## Parameters

- `in_control`: The   to remove from the clock device.

## See Also

- [AddControl](iouseraudioclockdevice/addcontrol.md)
  Adds a control to the clock device.
- [IOUserAudioControl](iouseraudiocontrol.md)
  The base class for audio control objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/removecontrol)*