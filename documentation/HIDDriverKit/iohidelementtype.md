# IOHIDElementType

**Framework**: HIDDriverKit  
**Kind**: enum

The types of HID elements that you can examine.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
enum IOHIDElementType : unsigned int;
```

#### Overview

Use this type to identify the type of an element you are using. The type is also the value for the key `kIOHIDElementTypeKey` in the dictionary describing the element.

## Topics

### Getting the Element Types
- [kIOHIDElementTypeInput_Misc](iohidelementtype/kiohidelementtypeinput_misc.md)
  The element contains an input data field of varying size.
- [kIOHIDElementTypeInput_Button](iohidelementtype/kiohidelementtypeinput_button.md)
  The element contains a one-bit input data field.
- [kIOHIDElementTypeInput_Axis](iohidelementtype/kiohidelementtypeinput_axis.md)
  The element contains an axis of movement.
- [kIOHIDElementTypeInput_ScanCodes](iohidelementtype/kiohidelementtypeinput_scancodes.md)
  The element contains an input field with a scan code or usage selector.
- [kIOHIDElementTypeInput_NULL](iohidelementtype/kiohidelementtypeinput_null.md)
  The element signals the end of an input data field in an input report.
- [kIOHIDElementTypeOutput](iohidelementtype/kiohidelementtypeoutput.md)
  The element contains a data field in an output report.
- [kIOHIDElementTypeFeature](iohidelementtype/kiohidelementtypefeature.md)
  The element contains input and output data not intended for consumption by the end user.
- [kIOHIDElementTypeCollection](iohidelementtype/kiohidelementtypecollection.md)
  The element acts as a parent container for two or more related elements.

## See Also

- [getType](iohidelement/gettype.md)
- [getCollectionType](iohidelement/getcollectiontype.md)
- [getChildElements](iohidelement/getchildelements.md)
- [getParentElement](iohidelement/getparentelement.md)
- [IOHIDElementCollectionType](iohidelementcollectiontype.md)
  Constants that indicate the types of relationships that exist between two or more elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelementtype)*