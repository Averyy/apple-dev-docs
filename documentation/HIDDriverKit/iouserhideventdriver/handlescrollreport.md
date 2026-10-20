# handleScrollReport

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Iterates through scroll elements and dispatches them if the element value has been updated.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void handleScrollReport(uint64_t timestamp, uint32_t reportID);
```

#### Discussion

This method iterates over the parsed scrolling elements and dispatches events for any changed values. The system calls this method automatically when a new report arrives; don’t call this method yourself.

## Parameters

- `timestamp`: The timestamp of the input report.
- `reportID`: The report ID.

## See Also

### Handling New Data Reports
- [handleReport](./handlereport.md)
  Processes the information in a new device report and dispatches any relevant events in response.
- [handleKeyboardReport](./handlekeyboardreport.md)
  Iterates through keyboard elements and dispatches them if the element value has been updated.
- [handleRelativePointerReport](./handlerelativepointerreport.md)
  Iterates through relative pointer elements and dispatches them if the element value has been updated.
- [handleAbsolutePointerReport](./handleabsolutepointerreport.md)
  Iterates through absolute pointer elements and dispatches them if the element value has been updated.
- [handleDigitizerReport](./handledigitizerreport.md)
  Processes the digitizer elements and dispatches events for any updated values.
- [createEventForDigitizerCollection](./createeventfordigitizercollection.md)
  Creates a HID event object that represents a digitizer collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver/handlescrollreport)*