# IOUserAudioCustomPropertyDataType

**Framework**: AudioDriverKit  
**Kind**: enum

A data and qualifier type used for custom properties.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioCustomPropertyDataType : uint32_t;
```

#### Discussion

Use `0` to indicate the custom property doesn’t have any data.

## Topics

### Data Types
- [Dictionary](audiodriverkit/iouseraudiocustompropertydatatype/dictionary.md)
  A data type that indicates the custom data is a dictionary.
- [String](audiodriverkit/iouseraudiocustompropertydatatype/string.md)
  A data type that indicates the custom data is a string.
### Enumeration Cases
- [None](audiodriverkit/iouseraudiocustompropertydatatype/none.md)

## See Also

- [Create](iouseraudiocustomproperty/create.md)
  Allocates and initializes an instance of the custom property class.
- [init](iouseraudiocustomproperty/init.md)
  Initializes an instance of a custom property.
- [IOUserAudioObjectPropertyAddress](audiodriverkit/iouseraudioobjectpropertyaddress.md)
  An object that collects the three parts — selector, scope, and element — that identify a specific property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiocustompropertydatatype)*