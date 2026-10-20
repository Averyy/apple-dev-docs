# GetBaseClassID

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the audio class identifier of the base class object.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual IOUserAudioClassID GetBaseClassID();
```

#### Return Value

The audio class identifier of the base class object.

## See Also

### Getting Information About the Class
- [GetClassID](./getclassid.md)
  Gets the audio class identifier of the object.
- [IOUserAudioClassID](../audiodriverkit-page/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetObjectID](./getobjectid.md)
  Gets the object’s identifier.
- [IOUserAudioObjectID](../audiodriverkit-page/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [GetWorkQueue](./getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/getbaseclassid)*