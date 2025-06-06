# parseLEDElement

**Framework**: HIDDriverKit  
**Kind**: method

Parses an element to see if it supports LED usages.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
bool parseLEDElement(IOHIDElement * element);
```

#### Return Value

`true` on success, otherwise `false`.

#### Discussion

This method checks the element to determine if it contains LED data suitable for dispatching in an event. If it does, the method stores a reference to the element for later use. When the driver object receives subsequent reports from the device, it uses the information in the stored LED elements to dispatch LED-specific events.

## Parameters

- `element`: An   object to parse.

## See Also

- [parseElements](iouserhideventdriver/parseelements.md)
  Parses the specified array of elements.
- [parsePointerElement](iouserhideventdriver/parsepointerelement.md)
  Parses an element to see if it supports pointer usages.
- [parseDigitizerElement](iouserhideventdriver/parsedigitizerelement.md)
  Parses an element to see if it supports digitizer usages.
- [parseKeyboardElement](iouserhideventdriver/parsekeyboardelement.md)
  Parses an element to see if it contains keyboard-related information.
- [parseScrollElement](iouserhideventdriver/parsescrollelement.md)
  Parses an element to see if it supports scroll usages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/parseledelement)*