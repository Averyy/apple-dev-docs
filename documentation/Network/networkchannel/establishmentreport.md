# establishmentReport()

**Framework**: Network  
**Kind**: method

Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, this method will wait until the connection becomes ready and then deliver the report. This method will start the connection if it isn’t already started.

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
func establishmentReport() async throws -> NWConnection.EstablishmentReport
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/establishmentreport())*