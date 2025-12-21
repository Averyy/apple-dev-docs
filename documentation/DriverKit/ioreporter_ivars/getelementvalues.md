# getElementValues

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
const IOReportElementValues * getElementValues(int element_index);
```

#### Return Value

A pointer to the element values requested or NULL on failure

#### Discussion

Internal method to directly access the values of an element

Locking: Caller must ensure that the reporter (data) lock is held. The returned pointer is only valid until unlockReporter() is called.

## Parameters

- `element_index`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/getelementvalues)*