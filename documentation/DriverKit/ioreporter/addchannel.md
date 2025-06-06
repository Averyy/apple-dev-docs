# addChannel

**Framework**: DriverKit  
**Kind**: method

Add an additional, similar channel to the reporter.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn addChannel(uint64_t channelID, const char * channelName);
```

#### Return Value

Appropriate `IOReturn` code.

#### Discussion

The reporter will allocate memory to track a new channel with the provided ID and name (if any). Its other traits (type, etc) will be those provided when the reporter was initialized.  If no channel name is provided and the channelID consists solely of ASCII bytes, those bytes (ignoring any NUL bytes) will be used as the human-readable channel name in user space.  The `IOREPORT_MAKEID()` macro in `IOReportTypes.h` can be used to create ASCII channel IDs.

Locking: same-instance concurrency SAFE, MAY BLOCK

## Parameters

- `channelID`: Identifier for the channel to be added.
- `channelName`: An optional human-readble name for the channel.

## See Also

- [configureReport](ioreporter/configurereport.md)
  Track IOService::configureReport(), provide sizing info
- [createLegend](ioreporter/createlegend.md)
  Create a legend entry represending this reporter’s channels.
- [free](ioreporter/free.md)
- [updateReport](ioreporter/updatereport.md)
  Produce standard reply to IOService::updateReport()


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter/addchannel)*