# AddControl

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds a control to the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t AddControl(IOUserAudioControl *in_control);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

If adding the control succeeds, the control’s reference count increments by one.

## Parameters

- `in_control`: The [`IOUserAudioControl`](../iouseraudiocontrol.md) to add to the clock device.

## See Also

### Managing Audio Controls
- [RemoveControl](./removecontrol.md)
  Removes a control from the clock device.
- [IOUserAudioControl](../iouseraudiocontrol.md)
  The base class for audio control objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/addcontrol)*