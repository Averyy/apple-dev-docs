# dataTransferReport()

**Framework**: Network  
**Kind**: method

Start a data transfer report on a connection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last). This method will start the connection if it isn’t already started.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func dataTransferReport() async throws -> NWConnection.DataTransferReport
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/datatransferreport())*