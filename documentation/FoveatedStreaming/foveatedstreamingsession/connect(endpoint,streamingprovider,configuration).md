# connect(endpoint:streamingProvider:configuration:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Role**: Instance Method

Establishes a streaming connection at the provided endpoint, passing connection parameters to the specified streaming provider.

**Availability**:
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
final func connect(endpoint: FoveatedStreamingSession.Endpoint = .systemDiscovered, streamingProvider: FoveatedStreamingSession.StreamingProvider, configuration: [String : FoveatedStreamingSession.ConfigurationValue]) async throws
```

## Discussion

Streaming providers can accept parameters specific to their streaming protocol — a video bitrate or codec selection, for example. The framework forwards the configuration to the provider without interpreting it. Consult your streaming provider’s documentation for the keys and values it accepts:

```swift
try await session.connect(
    endpoint: .local(ipAddress: address, port: port),
    streamingProvider: provider,
    configuration: [
        "com.example.MyProvider.maximumBitrateMbps": .int(150),
        "com.example.MyProvider.codec": .string("h265"),
    ]
)
```

> **Throws**: [`FoveatedStreamingSession.DisconnectReason`](./disconnectreason.md) if the connection fails, or `CancellationError` if the task is cancelled.

## Parameters

- `endpoint`: The endpoint to connect to (local IP, remote URL, or system-discovered).
- `streamingProvider`: The specific streaming provider to use for this connection.
- `configuration`: Connection parameters for the streaming provider. To have the provider apply its own defaults, use [`connect(endpoint:streamingProvider:)`](./connect%28endpoint,streamingprovider%29.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/connect(endpoint:streamingprovider:configuration:))*