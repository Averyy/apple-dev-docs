# handleIncrementChannelStateByIndices

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn handleIncrementChannelStateByIndices(int channel_index, int state_index, uint64_t time_in_state, uint64_t intransitions, uint64_t last_intransition);
```

#### Return Value

Appropriate IOReturn code

#### Discussion

Updates state data for a channel with passed arguments

Locked version of IOReporter::incrementChannelState(). This method may be overriden by sub-classes.

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `channel_index`: 
- `state_index`: 
- `time_in_state`: 
- `intransitions`: 
- `last_intransition`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iostatereporter_ivars/handleincrementchannelstatebyindices)*