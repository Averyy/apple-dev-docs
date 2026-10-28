# GetName

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the name of the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
OSSharedPtr<OSString> GetName();
```

## Return Value

A `OSSharedPtr` to an [`OSString`](../../DriverKit/osstring.md) containing the driver name.

## Discussion

Getting the name synchronizes by using the work queue created by the object.

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
- [SetName](./setname.md)
  Sets the name of the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/getname)*