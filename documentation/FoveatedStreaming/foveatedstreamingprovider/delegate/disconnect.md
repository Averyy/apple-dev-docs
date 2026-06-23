# disconnect()

**Framework**: Foveated Streaming  
**Kind**: method  
**Required**: Yes

Disconnect from the streaming endpoint.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func disconnect() async throws
```

#### Discussion

This method should cleanly shut down the streaming connection and release any associated resources.

This function will be called exactly once for the lifetime of the process.

> ⚠️ **Warning**: If the disconnect does not complete within a reasonable time, the process will be forcefully terminated.

> **Note**: If the disconnect does not complete cleanly.  The error will be presented to the host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/delegate/disconnect())*