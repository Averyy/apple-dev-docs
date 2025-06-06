# setElementValues

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn setElementValues(int element_index, IOReportElementValues * values, uint64_t record_time);
```

#### Return Value

IOReturn code

#### Discussion

Element_Index can be obtained from getFirstElementIndex().  If record_time is not provided, IOReporter::setElementValues() will fetch the current mach_absolute_time.  If the current time is already known, it is more efficient to pass it along.

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `element_index`: 
- `values`: 
- `record_time`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/setelementvalues)*