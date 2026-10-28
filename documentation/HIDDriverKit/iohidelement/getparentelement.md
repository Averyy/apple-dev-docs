# getParentElement

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual IOHIDElement * getParentElement();
```

## Return Value

Returns the parent element, if any.

## See Also

### Managing the Element Hierarchy
- [getType](./gettype.md)
- [getCollectionType](./getcollectiontype.md)
- [getChildElements](./getchildelements.md)
- [IOHIDElementType](../iohidelementtype.md)
  The types of HID elements that you can examine.
- [IOHIDElementCollectionType](../iohidelementcollectiontype.md)
  Constants that indicate the types of relationships that exist between two or more elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement/getparentelement)*