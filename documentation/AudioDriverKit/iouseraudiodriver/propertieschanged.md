# PropertiesChanged

**Framework**: AudioDriverKit  
**Kind**: method

Informs the host when the state of an object in the driver changes.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t PropertiesChanged(IOUserAudioObjectID in_object_id, IOUserAudioObjectPropertySelector * in_properties, uint32_t in_num_properties);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

For device objects, only use this method for state changes that don’t affect IO or the structure of the device.

## Parameters

- `in_object_id`: The identifier of the object whose properties changed.
- `in_properties`: An array of   instances for the changed properties.
- `in_num_properties`: The number of elements in the   array.

## See Also

- [IOUserAudioObjectPropertySelector](audiodriverkit/iouseraudioobjectpropertyselector.md)
  A four character code which, along with the scope and element, specific piece of information about an audio object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver/propertieschanged)*