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
IOReturn handleSetStateByIndices(int channel_index, int new_state_index, uint64_t last_intransition, uint64_t prev_state_residency);
```

#### Return Value

Appropriate IOReturn code

#### Discussion

Locked version of IOReporter::setStateByIndices().  This method may be overriden by sub-classes.

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `channel_index`: 
- `new_state_index`: 
- `last_intransition`: 
- `prev_state_residency`: 


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iostatereporter_ivars/handlesetstatebyindices)*