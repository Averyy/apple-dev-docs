# handleSetStateByIndices

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual IOReturn handleSetStateByIndices(int channel_index, int new_state_index, uint64_t last_intransition, uint64_t prev_state_residency);
```

#### Return Value

Appropriate IOReturn code

#### Discussion

Update a channel state without validating channel_id

Locked version of IOReporter::setStateByIndices().  This method may be overriden by sub-classes.

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `channel_index`: - 0.., available from getChannelIndex()
- `new_state_index`: - New state for the channel
- `last_intransition`: - to remove: time of most recent entry
- `prev_state_residency`: - to remove: time spent in previous state


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iostatereporter_ivars/handlesetstatebyindices)*