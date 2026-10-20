# RemoveObject

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes an audio object from the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t RemoveObject(IOUserAudioObject *in_object);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If the remove succeeds, the object’s reference count decrements by one. The caller should also call [`PropertiesChanged`](./propertieschanged.md) to notify the host of any changes.

## Parameters

- `in_object`: The [`IOUserAudioObjectID`](../audiodriverkit-page/iouseraudioobjectid.md) to remove from the driver.

## See Also

### Working with Audio Objects
- [AddObject](./addobject.md)
  Adds an audio object to the driver.
- [GetAudioObjectForObjectID](./getaudioobjectforobjectid.md)
  Gets a pointer to an audio object, given the object’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/removeobject)*