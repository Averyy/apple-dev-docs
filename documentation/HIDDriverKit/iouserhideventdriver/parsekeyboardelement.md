# parseKeyboardElement

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Parses an element to see if it contains keyboard-related information.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual bool parseKeyboardElement(IOHIDElement *element);
```

## Return Value

`true` if the element contains relevant keyboard information, or `false` if it doesn’t.

## Discussion

This method checks the element to determine if it contains keyboard data suitable for dispatching in an event. If it does, the method stores a reference to the element for later use. When the driver object receives subsequent reports from the device, it uses the information in the stored keyboard elements to dispatch keyboard-specific events.

## Parameters

- `element`: An `IOHIDElement` object to check.

## See Also

### Parsing the Element Hierarchy
- [parseElements](./parseelements.md)
  Parses the specified array of elements.
- [parsePointerElement](./parsepointerelement.md)
  Parses an element to see if it supports pointer usages.
- [parseDigitizerElement](./parsedigitizerelement.md)
  Parses an element to see if it supports digitizer usages.
- [parseScrollElement](./parsescrollelement.md)
  Parses an element to see if it supports scroll usages.
- [parseLEDElement](./parseledelement.md)
  Parses an element to see if it supports LED usages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/parsekeyboardelement)*