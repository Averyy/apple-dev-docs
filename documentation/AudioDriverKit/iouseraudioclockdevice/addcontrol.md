# AddControl

**Framework**: AudioDriverKit  
**Kind**: method

Adds a control to the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t AddControl(IOUserAudioControl * in_control);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If adding the control succeeds, the control’s reference count increments by one.

## Parameters

- `in_control`: The   to add to the clock device.

## See Also

- [RemoveControl](iouseraudioclockdevice/removecontrol.md)
  Removes a control from the clock device.
- [IOUserAudioControl](iouseraudiocontrol.md)
  The base class for audio control objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/addcontrol)*