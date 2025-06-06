# updateReportChannel

**Framework**: DriverKit  
**Kind**: method

Internal method to extract channel data to a destination.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn updateReportChannel(int channel_index, uint32_t & elementCount, uint8_t * & buffer, size_t & capacity);
```

#### Return Value

Appropriate [`IOReturn`](ioreturn.md) code

#### Discussion

Used to extract a single channel’s data to the updateReport() destination.

Locking: Caller must ensure that the reporter (data) lock is held.

## Parameters

- `channel_index`: Offset into internal elements array
- `elementCount`: Incremented by the number of IOReportElements added
- `buffer`: Buffer.
- `capacity`: Capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/updatereportchannel)*