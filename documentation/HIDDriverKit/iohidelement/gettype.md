# getType

**Framework**: HIDDriverKit  
**Kind**: method

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
IOHIDElementType getType();
```

#### Return Value

Returns the element type. Types are defined by the IOHIDElementType enumerator in [`IOHIDElementType`](iohidelementtype.md).

## See Also

- [getCollectionType](iohidelement/getcollectiontype.md)
- [getChildElements](iohidelement/getchildelements.md)
- [getParentElement](iohidelement/getparentelement.md)
- [IOHIDElementType](iohidelementtype.md)
  The types of HID elements that you can examine.
- [IOHIDElementCollectionType](iohidelementcollectiontype.md)
  Constants that indicate the types of relationships that exist between two or more elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement/gettype)*