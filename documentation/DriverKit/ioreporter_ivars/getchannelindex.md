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
virtual IOReturn getChannelIndex(uint64_t channel_id, int *channel_index);
```

#### Return Value

Appropriate IOReturn code

#### Discussion

Returns the index of a channel from internal data structures

For efficiently and thread-safely reading channels

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `channel_id`: - ID of the channel
- `channel_index`: - pointer to the returned element_index


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/getchannelindex)*