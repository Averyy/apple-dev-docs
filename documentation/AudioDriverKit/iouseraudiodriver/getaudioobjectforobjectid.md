# GetAudioObjectForObjectID

**Framework**: AudioDriverKit  
**Kind**: method

Gets a pointer to an audio object, given the object’s identifier.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
OSSharedPtr<IOUserAudioObject> GetAudioObjectForObjectID(IOUserAudioObjectID in_object_id);
```

#### Return Value

An `OSSharedPtr` to an [`IOUserAudioObject`](iouseraudioobject.md) if `in_object_id` was found.

## Parameters

- `in_object_id`: The   of an object previously added to the driver.

## See Also

- [AddObject](iouseraudiodriver/addobject.md)
  Adds an audio object to the driver.
- [RemoveObject](iouseraudiodriver/removeobject.md)
  Removes an audio object from the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/getaudioobjectforobjectid)*