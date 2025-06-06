# handleReport

**Framework**: HIDDriverKit  
**Kind**: method

Processes the information in a new device report and dispatches any relevant events in response.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void handleReport(uint64_t timestamp, uint8_t * report, uint32_t reportLength, IOHIDReportType type, uint32_t reportID);
```

#### Discussion

This method iterates over the elements in the report and dispatches events for any changed values. The system calls this method automatically when a new report arrives; don’t call this method yourself.

## Parameters

- `timestamp`: The timestamp of the report.
- `report`: A pointer to the raw bytes of the report.
- `reportLength`: The number of bytes of data in the   parameter.
- `type`: The report type.
- `reportID`: The unique ID associated with the report. If a report element has new data, it contains this ID.

## See Also

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
- [createEventForDigitizerCollection](iouserhideventdriver/createeventfordigitizercollection.md)
  Creates a HID event object that represents a digitizer collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/handlereport)*