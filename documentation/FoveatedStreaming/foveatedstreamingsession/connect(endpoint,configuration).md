# connect(endpoint:configuration:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Role**: Instance Method

Establishes a streaming connection at the provided endpoint, passing connection parameters to the system-default streaming provider.

**Availability**:
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
final func connect(endpoint: FoveatedStreamingSession.Endpoint = .systemDiscovered, configuration: [String : FoveatedStreamingSession.ConfigurationValue]) async throws
```

## Discussion

Use this when you haven’t selected a provider explicitly but still need to configure the one the system uses. To choose the provider yourself, use [`connect(endpoint:streamingProvider:configuration:)`](./connect%28endpoint,streamingprovider,configuration%29.md).

> **Throws**: A [`FoveatedStreamingSession.DisconnectReason`](./disconnectreason.md) error if a disconnection occurs.  Or, a [`CancellationError`](../../Swift/cancellationerror.md) if the task is cancelled.

## Parameters

- `endpoint`: The streaming endpoint to connect to.
- `configuration`: Connection parameters for the streaming provider. To have the provider apply its own defaults, use [`connect(endpoint:)`](./connect%28endpoint%29.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/connect(endpoint:configuration:))*