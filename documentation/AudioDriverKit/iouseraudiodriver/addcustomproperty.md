# AddCustomProperty

**Framework**: AudioDriverKit  
**Kind**: method

Adds a custom property object to the driver.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t AddCustomProperty(IOUserAudioCustomProperty * in_custom_property);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `in_custom_property`: An   object to add to the  .

## See Also

- [RemoveCustomProperty](iouseraudiodriver/removecustomproperty.md)
  Removes a previously-added custom property object from the driver.
- [IOUserAudioCustomProperty](iouseraudiocustomproperty.md)
  A custom property to associate with audio objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/addcustomproperty)*