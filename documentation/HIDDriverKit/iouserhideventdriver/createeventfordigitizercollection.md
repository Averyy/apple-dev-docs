# createEventForDigitizerCollection

**Framework**: HIDDriverKit  
**Kind**: method

Creates a HID event object that represents a digitizer collection.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
IOHIDEvent * createEventForDigitizerCollection(IOHIDDigitizerCollection * collection, uint64_t timestamp, uint32_t reportID);
```

#### Return Value

An `IOHIDEvent` object containing the digitizer-related data. This method returns `NULL` if it encounters an error or if no elements in the collection contain updated values.

#### Discussion

This method creates an `IOHIDEvent` object with any updated digitizer values that it finds. The [`handleDigitizerReport`](iouserhideventdriver/handledigitizerreport.md) calls this method when processing an input report; don’t call this method directly.

## Parameters

- `collection`: A collection of   objects, each of which contains digitizer information to include in the event object.
- `timestamp`: The timestamp of the input report.
- `reportID`: The report ID.

## See Also

- [handleReport](iouserhideventdriver/handlereport.md)
  Processes the information in a new device report and dispatches any relevant events in response.
- [handleKeyboardReport](iouserhideventdriver/handlekeyboardreport.md)
  Iterates through keyboard elements and dispatches them if the element value has been updated.
- [handleRelativePointerReport](iouserhideventdriver/handlerelativepointerreport.md)
  Iterates through relative pointer elements and dispatches them if the element value has been updated.
- [handleAbsolutePointerReport](iouserhideventdriver/handleabsolutepointerreport.md)
  Iterates through absolute pointer elements and dispatches them if the element value has been updated.
- [handleScrollReport](iouserhideventdriver/handlescrollreport.md)
  Iterates through scroll elements and dispatches them if the element value has been updated.
- [handleDigitizerReport](iouserhideventdriver/handledigitizerreport.md)
  Processes the digitizer elements and dispatches events for any updated values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/createeventfordigitizercollection)*