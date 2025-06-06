# IOUserAudioCustomPropertyInfo

**Framework**: AudioDriverKit  
**Kind**: struct

A description of a custom property’s data types.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
struct IOUserAudioCustomPropertyInfo;
```

#### Discussion

The description provided by the [`IOUserAudioCustomPropertyInfo`](audiodriverkit/iouseraudiocustompropertyinfo.md) structure allows the host to marshal the data between the host and its clients.

## Topics

### Property Metadata
- [mSelector](audiodriverkit/iouseraudiocustompropertyinfo/mselector.md)
  The property selector of the custom property.
- [mPropertyDataType](audiodriverkit/iouseraudiocustompropertyinfo/mpropertydatatype.md)
  The data type of the of the custom property’s data.
- [mQualifierDataType](audiodriverkit/iouseraudiocustompropertyinfo/mqualifierdatatype.md)
  The data type of the of the custom property’s qualifier data.

## See Also

- [SetQualifierAndDataValue](iouseraudiocustomproperty/setqualifieranddatavalue.md)
  Sets the custom property’s data value.
- [GetCustomPropertyValueWithQualifier](iouseraudiocustomproperty/getcustompropertyvaluewithqualifier.md)
  Gets the custom property value for a given qualifier.
- [GetCustomPropertyInfo](iouseraudiocustomproperty/getcustompropertyinfo.md)
  Gets a property info object that describes the custom property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiocustompropertyinfo)*