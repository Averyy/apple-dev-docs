# GetClassID

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the audio class identifier of the object.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual IOUserAudioClassID GetClassID();
```

## Return Value

The audio class identifier of the object.

## See Also

### Getting Information About the Class
- [GetBaseClassID](./getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](../audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetObjectID](./getobjectid.md)
  Gets the object’s identifier.
- [IOUserAudioObjectID](../audiodriverkit-page/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [GetWorkQueue](./getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/getclassid)*