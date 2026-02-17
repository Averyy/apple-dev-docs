# remote(serverName:)

**Framework**: Foveated Streaming  
**Kind**: method

Connects to a remote endpoint by server name.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
static func remote(serverName: String) -> FoveatedStreamingSession.Endpoint
```

#### Discussion

The framework uses the server name to look up the remote URL from the app’s [`ApprovedStreamingEndpoints`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ApprovedStreamingEndpoints) in `Info.plist`.

## Parameters

- `serverName`: The server name corresponding to an entry in the   dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/endpoint/remote(servername:))*