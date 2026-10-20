# GetObjectID

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the object’s identifier.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
IOUserAudioObjectID GetObjectID();
```

#### Return Value

The object’s `IOUserAudioObjectID`.

#### Discussion

Use this identifier when looking up a driver’s objects with [`GetAudioObjectForObjectID`](../iouseraudiodriver/getaudioobjectforobjectid.md).

## See Also

### Getting Information About the Class
- [GetClassID](./getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](./getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](../audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [IOUserAudioObjectID](../audiodriverkit-page/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [GetWorkQueue](./getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/getobjectid)*