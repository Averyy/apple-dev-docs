# connect(endpoint:streamingProvider:)

**Framework**: Foveated Streaming  
**Kind**: method

Establishes a streaming connection at the provided endpoint using the specified streaming provider.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func connect(endpoint: FoveatedStreamingSession.Endpoint = .systemDiscovered, streamingProvider: FoveatedStreamingSession.StreamingProvider) async throws
```

#### Discussion

This overload allows you to explicitly specify which streaming provider extension to use.

> **Note**: [`FoveatedStreamingSession.DisconnectReason`](foveatedstreamingsession/disconnectreason.md) if the connection fails, or `CancellationError` if the task is cancelled.

## Parameters

- `endpoint`: The endpoint to connect to (local IP, remote URL, or system-discovered).
- `streamingProvider`: The specific streaming provider to use for this connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/connect(endpoint:streamingprovider:))*