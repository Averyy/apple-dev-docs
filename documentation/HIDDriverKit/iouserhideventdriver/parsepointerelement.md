# parsePointerElement

**Framework**: HIDDriverKit  
**Kind**: method

Parses an element to see if it supports pointer usages.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
bool parsePointerElement(IOHIDElement * element);
```

#### Return Value

`true` on success, otherwise `false`.

#### Discussion

This method checks the element to determine if it contains pointer data suitable for dispatching in an event. If it does, the method stores a reference to the element for later use. When the driver object receives subsequent reports from the device, it uses the information in the stored pointer elements to dispatch pointer-specific events.

## Parameters

- `element`: An   object to parse.

## See Also

- [parseElements](iouserhideventdriver/parseelements.md)
  Parses the specified array of elements.
- [parseDigitizerElement](iouserhideventdriver/parsedigitizerelement.md)
  Parses an element to see if it supports digitizer usages.
- [parseKeyboardElement](iouserhideventdriver/parsekeyboardelement.md)
  Parses an element to see if it contains keyboard-related information.
- [parseScrollElement](iouserhideventdriver/parsescrollelement.md)
  Parses an element to see if it supports scroll usages.
- [parseLEDElement](iouserhideventdriver/parseledelement.md)
  Parses an element to see if it supports LED usages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/parsepointerelement)*