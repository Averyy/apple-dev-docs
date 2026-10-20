# RemoveCustomProperty

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Attempts to remove a custom property from the custom property.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t RemoveCustomProperty(IOUserAudioCustomProperty *in_custom_property);
```

#### Return Value

[`kIOReturnError`](../../DriverKit/kioreturnerror.md)

#### Discussion

This method always returns [`kIOReturnError`](../../DriverKit/kioreturnerror.md) since a custom property can’t have a custom property.

## Parameters

- `in_custom_property`: An [`IOUserAudioCustomProperty`](../iouseraudiocustomproperty.md) object to remove from the [`IOUserAudioCustomProperty`](../iouseraudiocustomproperty.md).

## See Also

### Infrequently Used Functionality
- [AddCustomProperty](./addcustomproperty.md)
  Attempts to add a custom property to the custom property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/removecustomproperty)*