# AddObject

**Framework**: AudioDriverKit  
**Kind**: method

Adds an audio object to the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t AddObject(IOUserAudioObject * in_object);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Use this method to add to the driver any objects that require management by the host. If the add succeeds, the object’s reference count increments by one. The caller should also call [`PropertiesChanged`](iouseraudiodriver/propertieschanged.md) to notify the host of any changes.

## Parameters

- `in_object`: The   to add to the driver.

## See Also

- [RemoveObject](iouseraudiodriver/removeobject.md)
  Removes an audio object from the driver.
- [GetAudioObjectForObjectID](iouseraudiodriver/getaudioobjectforobjectid.md)
  Gets a pointer to an audio object, given the object’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/addobject)*