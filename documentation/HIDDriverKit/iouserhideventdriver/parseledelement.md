# parseLEDElement

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Parses an element to see if it supports LED usages.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual bool parseLEDElement(IOHIDElement *element);
```

## Return Value

`true` on success, otherwise `false`.

## Discussion

This method checks the element to determine if it contains LED data suitable for dispatching in an event. If it does, the method stores a reference to the element for later use. When the driver object receives subsequent reports from the device, it uses the information in the stored LED elements to dispatch LED-specific events.

## Parameters

- `element`: An `IOHIDElement` object to parse.

## See Also

### Parsing the Element Hierarchy
- [parseElements](./parseelements.md)
  Parses the specified array of elements.
- [parsePointerElement](./parsepointerelement.md)
  Parses an element to see if it supports pointer usages.
- [parseDigitizerElement](./parsedigitizerelement.md)
  Parses an element to see if it supports digitizer usages.
- [parseKeyboardElement](./parsekeyboardelement.md)
  Parses an element to see if it contains keyboard-related information.
- [parseScrollElement](./parsescrollelement.md)
  Parses an element to see if it supports scroll usages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/parseledelement)*