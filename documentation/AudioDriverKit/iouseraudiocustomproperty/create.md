# Create

**Framework**: AudioDriverKit  
**Kind**: method

Allocates and initializes an instance of the custom property class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
static OSSharedPtr<IOUserAudioCustomProperty> Create(IOUserAudioDriver * in_audio_driver, IOUserAudioObjectPropertyAddress in_prop_addr, bool in_is_property_settable, IOUserAudioCustomPropertyDataType in_qualifier_data_type, IOUserAudioCustomPropertyDataType in_data_type);
```

#### Return Value

A poiner to an [`IOUserAudioCustomProperty`](iouseraudiocustomproperty.md), if allocation and initialization succeeded.

#### Discussion

If you subclass [`IOUserAudioCustomProperty`](iouseraudiocustomproperty.md) to override this class’ behavior, don’t use [`Create`](iouseraudiocustomproperty/create.md) to allocate and initialize the custom subclass.

## Parameters

- `in_audio_driver`: The   that owns this object.
- `in_prop_addr`:   of the custom property.
- `in_is_property_settable`: A Boolean value that indicates if the property can be set.
- `in_qualifier_data_type`: The   for custom property’s qualifier data value.
- `in_data_type`: The   for custom property’s data value.This value can’t be  .

## See Also

- [init](iouseraudiocustomproperty/init.md)
  Initializes an instance of a custom property.
- [IOUserAudioObjectPropertyAddress](audiodriverkit/iouseraudioobjectpropertyaddress.md)
  An object that collects the three parts — selector, scope, and element — that identify a specific property.
- [IOUserAudioCustomPropertyDataType](audiodriverkit/iouseraudiocustompropertydatatype.md)
  A data and qualifier type used for custom properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/create)*