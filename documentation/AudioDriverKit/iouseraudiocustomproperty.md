# IOUserAudioCustomProperty

**Framework**: AudioDriverKit  
**Kind**: class

A custom property to associate with audio objects.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioCustomProperty;
```

#### Overview

Along with the property value, you can provide a qualifier value to further refine get and set operations. For example, if a given property exists on multiple devices, use a device identifier as the qualifier to indicate which device to set the value on.

## Topics

### Creating a Custom Property
- [Create](iouseraudiocustomproperty/create.md)
  Allocates and initializes an instance of the custom property class.
- [init](iouseraudiocustomproperty/init.md)
  Initializes an instance of a custom property.
- [IOUserAudioObjectPropertyAddress](audiodriverkit/iouseraudioobjectpropertyaddress.md)
  An object that collects the three parts — selector, scope, and element — that identify a specific property.
- [IOUserAudioCustomPropertyDataType](audiodriverkit/iouseraudiocustompropertydatatype.md)
  A data and qualifier type used for custom properties.
### Freeing a Custom Property
- [free](iouseraudiocustomproperty/free.md)
  Frees the custom property.
### Getting Information About the Class
- [GetClassID](iouseraudiocustomproperty/getclassid.md)
  Gets the audio class identifier of the object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Supporting Data Value Changes
- [HandleChangeCustomPropertyDataValueWithQualifier](iouseraudiocustomproperty/handlechangecustompropertydatavaluewithqualifier.md)
  Tells the property the data value is changing.
### Accessing the Data Value
- [SetQualifierAndDataValue](iouseraudiocustomproperty/setqualifieranddatavalue.md)
  Sets the custom property’s data value.
- [GetCustomPropertyValueWithQualifier](iouseraudiocustomproperty/getcustompropertyvaluewithqualifier.md)
  Gets the custom property value for a given qualifier.
- [GetCustomPropertyInfo](iouseraudiocustomproperty/getcustompropertyinfo.md)
  Gets a property info object that describes the custom property.
- [IOUserAudioCustomPropertyInfo](audiodriverkit/iouseraudiocustompropertyinfo.md)
  A description of a custom property’s data types.
### Infrequently Used Functionality
- [AddCustomProperty](iouseraudiocustomproperty/addcustomproperty.md)
  Attempts to add a custom property to the custom property.
- [RemoveCustomProperty](iouseraudiocustomproperty/removecustomproperty.md)
  Attempts to remove a custom property from the custom property.

## Relationships

### Inherits From
- [IOUserAudioObject](iouseraudioobject.md)

## See Also

- [AddCustomProperty](iouseraudiodriver/addcustomproperty.md)
  Adds a custom property object to the driver.
- [RemoveCustomProperty](iouseraudiodriver/removecustomproperty.md)
  Removes a previously-added custom property object from the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocustomproperty)*