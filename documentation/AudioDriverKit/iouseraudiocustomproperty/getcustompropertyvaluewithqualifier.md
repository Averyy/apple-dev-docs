# GetCustomPropertyValueWithQualifier

**Framework**: AudioDriverKit  
**Kind**: method

Gets the custom property value for a given qualifier.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t GetCustomPropertyValueWithQualifier(OSObject * in_qualifier_data, OSObject * * out_data);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Use this method to get the custom property’s data value, optionally adding a qualifier to further refine the action. For example, if a given property exists on multiple devices, use a device identifier as the qualifier to indicate which device to get the value from.

The base class returns the custom property value set on the object without looking at contents of the qualifier data. If the returned value should depend on the qualifier, subclass [`IOUserAudioCustomProperty`](iouseraudiocustomproperty.md) and override this method.

## Parameters

- `in_qualifier_data`: The property qualifier, as an  . The caller retains and releases this object. This value is   if the qualifier data type is  .
- `out_data`: On output, the property value, as an  . The caller retains and releases this object.

## See Also

- [SetQualifierAndDataValue](iouseraudiocustomproperty/setqualifieranddatavalue.md)
  Sets the custom property’s data value.
- [GetCustomPropertyInfo](iouseraudiocustomproperty/getcustompropertyinfo.md)
  Gets a property info object that describes the custom property.
- [IOUserAudioCustomPropertyInfo](audiodriverkit/iouseraudiocustompropertyinfo.md)
  A description of a custom property’s data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty/getcustompropertyvaluewithqualifier)*