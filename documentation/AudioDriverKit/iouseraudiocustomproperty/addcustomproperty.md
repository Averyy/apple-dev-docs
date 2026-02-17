# AddCustomProperty

**Framework**: AudioDriverKit  
**Kind**: method

Attempts to add a custom property to the custom property.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
virtual kern_return_t AddCustomProperty(IOUserAudioCustomProperty *in_custom_property);
```

#### Return Value

[`kIOReturnError`](https://developer.apple.com/documentation/DriverKit/kIOReturnError)

#### Discussion

This method always returns [`kIOReturnError`](https://developer.apple.com/documentation/DriverKit/kIOReturnError) since a custom property can’t have a custom property.

## Parameters

- `in_custom_property`: An   object to add to the  .

## See Also

- [RemoveCustomProperty](iouseraudiocustomproperty/removecustomproperty.md)
  Attempts to remove a custom property from the custom property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/addcustomproperty)*