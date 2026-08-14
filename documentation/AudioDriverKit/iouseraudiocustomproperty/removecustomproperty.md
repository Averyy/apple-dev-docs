# RemoveCustomProperty

**Framework**: AudioDriverKit  
**Kind**: method

Attempts to remove a custom property from the custom property.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
virtual kern_return_t RemoveCustomProperty(IOUserAudioCustomProperty *in_custom_property);
```

#### Return Value

[`kIOReturnError`](https://developer.apple.com/documentation/driverkit/kioreturnerror)

#### Discussion

This method always returns [`kIOReturnError`](https://developer.apple.com/documentation/driverkit/kioreturnerror) since a custom property can’t have a custom property.

## Parameters

- `in_custom_property`: An [`IOUserAudioCustomProperty`](iouseraudiocustomproperty.md) object to remove from the [`IOUserAudioCustomProperty`](iouseraudiocustomproperty.md).

## See Also

- [AddCustomProperty](iouseraudiocustomproperty/addcustomproperty.md)
  Attempts to add a custom property to the custom property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/removecustomproperty)*