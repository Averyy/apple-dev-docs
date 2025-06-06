# getChannelIndex

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn getChannelIndex(uint64_t channel_id, int * channel_index);
```

#### Return Value

Appropriate IOReturn code

#### Discussion

For efficiently and thread-safely reading channels

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `channel_id`: 
- `channel_index`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/getchannelindex)*