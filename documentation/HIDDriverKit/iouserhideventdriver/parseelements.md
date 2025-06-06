# parseElements

**Framework**: HIDDriverKit  
**Kind**: method

Parses the specified array of elements.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
bool parseElements(OSArray * elements);
```

#### Return Value

`true` if parsing was successful, or `false` if an error occurred.

#### Discussion

This method searches the elements array for [`IOHIDElement`](iohidelement.md) objects relevant to keyboard, digitizer, pointer, scrolling, and LED events. It stores a reference to each relevant element it finds, and uses those objects later to obtain relevant information for events.

The driver’s [`Start`](iouserhideventdriver/start.md) method calls this method, so you don’t need to call it directly.

## Parameters

- `elements`: An array of   objects to parse.

## See Also

- [parsePointerElement](iouserhideventdriver/parsepointerelement.md)
  Parses an element to see if it supports pointer usages.
- [parseDigitizerElement](iouserhideventdriver/parsedigitizerelement.md)
  Parses an element to see if it supports digitizer usages.
- [parseKeyboardElement](iouserhideventdriver/parsekeyboardelement.md)
  Parses an element to see if it contains keyboard-related information.
- [parseScrollElement](iouserhideventdriver/parsescrollelement.md)
  Parses an element to see if it supports scroll usages.
- [parseLEDElement](iouserhideventdriver/parseledelement.md)
  Parses an element to see if it supports LED usages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/parseelements)*