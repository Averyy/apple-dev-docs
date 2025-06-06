# SetName

**Framework**: AudioDriverKit  
**Kind**: method

Sets the name of the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetName(OSString * in_name);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If the change succeeds, the framework sends a notification to the host to update its object state. Setting the name synchronizes by using the work queue created by the object.

## Parameters

- `in_name`: The name to set, as an  .

## See Also

- [GetClassID](iouseraudiodriver/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiodriver/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetWorkQueue](iouseraudiodriver/getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.
- [GetName](iouseraudiodriver/getname.md)
  Gets the name of the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/setname)*