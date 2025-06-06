# RemoveObject

**Framework**: AudioDriverKit  
**Kind**: method

Removes an audio object from the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t RemoveObject(IOUserAudioObject * in_object);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If the remove succeeds, the object’s reference count decrements by one. The caller should also call [`PropertiesChanged`](iouseraudiodriver/propertieschanged.md) to notify the host of any changes.

## Parameters

- `in_object`: The   to remove from the driver.

## See Also

- [AddObject](iouseraudiodriver/addobject.md)
  Adds an audio object to the driver.
- [GetAudioObjectForObjectID](iouseraudiodriver/getaudioobjectforobjectid.md)
  Gets a pointer to an audio object, given the object’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/removeobject)*