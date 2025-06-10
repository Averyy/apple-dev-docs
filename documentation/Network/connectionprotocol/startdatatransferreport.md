# startDataTransferReport()

**Framework**: Network  
**Kind**: method

Start a new pending data transfer report on a connection. Multiple reports may be created for a single NWConnection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func startDataTransferReport() -> NWConnection.PendingDataTransferReport
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/connectionprotocol/startdatatransferreport())*