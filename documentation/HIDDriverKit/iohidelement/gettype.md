# getType

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual IOHIDElementType getType();
```

#### Return Value

Returns the element type. Types are defined by the IOHIDElementType enumerator in [`IOHIDElementType`](../iohidelementtype.md).

## See Also

### Managing the Element Hierarchy
- [getCollectionType](./getcollectiontype.md)
- [getChildElements](./getchildelements.md)
- [getParentElement](./getparentelement.md)
- [IOHIDElementType](../iohidelementtype.md)
  The types of HID elements that you can examine.
- [IOHIDElementCollectionType](../iohidelementcollectiontype.md)
  Constants that indicate the types of relationships that exist between two or more elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement/gettype)*