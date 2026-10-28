# AddObject

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds an audio object to the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t AddObject(IOUserAudioObject *in_object);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Use this method to add to the driver any objects that require management by the host. If the add succeeds, the object’s reference count increments by one. The caller should also call [`PropertiesChanged`](./propertieschanged.md) to notify the host of any changes.

## Parameters

- `in_object`: The [`IOUserAudioObjectID`](../audiodriverkit-page/iouseraudioobjectid.md) to add to the driver.

## See Also

### Working with Audio Objects
- [RemoveObject](./removeobject.md)
  Removes an audio object from the driver.
- [GetAudioObjectForObjectID](./getaudioobjectforobjectid.md)
  Gets a pointer to an audio object, given the object’s identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/addobject)*