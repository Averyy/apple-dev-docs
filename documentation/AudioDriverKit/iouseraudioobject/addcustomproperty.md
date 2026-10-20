# AddCustomProperty

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds a custom property to the audio object.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t AddCustomProperty(IOUserAudioCustomProperty *in_custom_property);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `in_custom_property`: An [`IOUserAudioCustomProperty`](../iouseraudiocustomproperty.md) object to add to the [`IOUserAudioObject`](../iouseraudioobject.md).

## See Also

### Using Custom Properties
- [RemoveCustomProperty](./removecustomproperty.md)
  Removes a previously-added custom property object from the audio object.
- [IOUserAudioCustomProperty](../iouseraudiocustomproperty.md)
  A custom property to associate with audio objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/addcustomproperty)*