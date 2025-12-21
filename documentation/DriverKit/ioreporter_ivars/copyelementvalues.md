# copyElementValues

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn copyElementValues(int element_index, IOReportElementValues * elementValues);
```

#### Return Value

Returns the content of an element

#### Discussion

Copies the values of an internal element to *elementValues

For efficiently and thread-safely reading _elements. May need to find the index of the element first.

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `element_index`: 
- `elementValues`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/copyelementvalues)*