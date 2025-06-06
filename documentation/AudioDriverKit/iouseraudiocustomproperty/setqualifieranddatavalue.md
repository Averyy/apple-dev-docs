# SetQualifierAndDataValue

**Framework**: AudioDriverKit  
**Kind**: method

Sets the custom property’s data value.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetQualifierAndDataValue(OSObject * in_qualifier_data, OSObject * in_data);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Use this method to set the custom property’s data value, optionally adding a qualifier to further refine the action. For example, if a given property exists on multiple devices, use a device identifier as the qualifier to indicate which device to set the value on.

## Parameters

- `in_qualifier_data`: The qualifier data for the custom property that corresponds to the data value. The type of this parameter must match the qualifier data type originally used for initializing the property. If the qualifier data type is  , this parameter must be  . If the qualifier data type is  , this parameter must be an  . If the qualifier data type is  , this parameter must be an  .
- `in_data`: The data object for the custom property that corresponds to the qualifier. The type of this parameter must match the data type originally used for initializing the property. If the data type is  , this parameter must be an  . If the qualifier data type is  , this parameter must be an  . This parameter can’t be  .

## See Also

- [GetCustomPropertyValueWithQualifier](iouseraudiocustomproperty/getcustompropertyvaluewithqualifier.md)
  Gets the custom property value for a given qualifier.
- [GetCustomPropertyInfo](iouseraudiocustomproperty/getcustompropertyinfo.md)
  Gets a property info object that describes the custom property.
- [IOUserAudioCustomPropertyInfo](audiodriverkit/iouseraudiocustompropertyinfo.md)
  A description of a custom property’s data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/setqualifieranddatavalue)*