# GetObjectID

**Framework**: AudioDriverKit  
**Kind**: method

Gets the object’s identifier.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
IOUserAudioObjectID GetObjectID();
```

#### Return Value

The object’s `IOUserAudioObjectID`.

#### Discussion

Use this identifier when looking up a driver’s objects with [`GetAudioObjectForObjectID`](iouseraudiodriver/getaudioobjectforobjectid.md).

## See Also

- [GetClassID](iouseraudioobject/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudioobject/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [IOUserAudioObjectID](audiodriverkit/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [GetWorkQueue](iouseraudioobject/getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/getobjectid)*