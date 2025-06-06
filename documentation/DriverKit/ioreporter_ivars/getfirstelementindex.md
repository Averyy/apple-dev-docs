# getFirstElementIndex

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn getFirstElementIndex(uint64_t channel_id, int * element_index);
```

#### Return Value

Appropriate IOReturn code

#### Discussion

For efficiently and thread-safely reading _elements

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `channel_id`: 
- `element_index`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/getfirstelementindex)*