# RemoveCustomProperty

**Framework**: AudioDriverKit  
**Kind**: method

Removes a previously-added custom property object from the audio object.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t RemoveCustomProperty(IOUserAudioCustomProperty * in_custom_property);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `in_custom_property`: An   object to remove from the  .

## See Also

- [AddCustomProperty](iouseraudioobject/addcustomproperty.md)
  Adds a custom property to the audio object.
- [IOUserAudioCustomProperty](iouseraudiocustomproperty.md)
  A custom property to associate with audio objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject/removecustomproperty)*