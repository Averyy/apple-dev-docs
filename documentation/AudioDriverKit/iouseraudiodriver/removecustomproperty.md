# RemoveCustomProperty

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes a previously-added custom property object from the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t RemoveCustomProperty(IOUserAudioCustomProperty *in_custom_property);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `in_custom_property`: An [`IOUserAudioCustomProperty`](../iouseraudiocustomproperty.md) object to remove from the [`IOUserAudioDriver`](../iouseraudiodriver.md).

## See Also

### Working with Custom Properties
- [AddCustomProperty](./addcustomproperty.md)
  Adds a custom property object to the driver.
- [IOUserAudioCustomProperty](../iouseraudiocustomproperty.md)
  A custom property to associate with audio objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/removecustomproperty)*