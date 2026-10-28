# GetWorkQueue

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the work queue created by the audio object, as a pointer to a dispatch queue.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
OSSharedPtr<IODispatchQueue> GetWorkQueue();
```

## Return Value

The work queue created by the audio object.

## Discussion

The work queue synchronizes access to the driver’s state. Setters and getters for the object do their work on the work queue.

## See Also

### Getting Information About the Class
- [GetClassID](./getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](./getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](../audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetObjectID](./getobjectid.md)
  Gets the object’s identifier.
- [IOUserAudioObjectID](../audiodriverkit-page/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/getworkqueue)*