# SetName

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the name of the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetName(OSString *in_name);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If the change succeeds, the framework sends a notification to the host to update its object state. Setting the name synchronizes by using the work queue created by the object.

## Parameters

- `in_name`: The name to set, as an [`OSString`](../../DriverKit/osstring.md).

## See Also

### Getting Information About the Class
- [GetClassID](./getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](./getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](../audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetWorkQueue](./getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.
- [GetName](./getname.md)
  Gets the name of the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/setname)*