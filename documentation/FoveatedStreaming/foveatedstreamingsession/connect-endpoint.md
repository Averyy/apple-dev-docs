# connect(endpoint:)

**Framework**: Foveated Streaming  
**Kind**: method

Establishes a streaming connection at the provided endpoint.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
@MainActor
final func connect(endpoint: FoveatedStreamingSession.Endpoint = .systemDiscovered) async throws
```

#### Discussion

> **Note**: A [`FoveatedStreamingSession.DisconnectReason`](foveatedstreamingsession/disconnectreason.md) error if a disconnection occurs.  Or, a [`CancellationError`](https://developer.apple.com/documentation/swift/cancellationerror) if the task is cancelled.

You can establish a streaming connection in a variety of ways:

```swift
// Connect by discovering nearby endpoints.
try await session.connect(endpoint: .systemDiscovered)

// Connect directly with IP address and port number.
try await session.connect(endpoint: .local(ipAddress: "125.125.125.125", port: 55000))

// Connect to a remote cloud endpoint by specifying a server name
// which corresponds to an entry in the `ApprovedStreamingEndpoints` dictionary in Info.plist.
try await session.connect(endpoint: .remote(serverName: "My Remote Server", signalingHeaders: ["test-header": "my-test"])
```

You can stop establishing a connection by cancelling the task or calling [`disconnect()`](foveatedstreamingsession/disconnect().md).

## Parameters

- `endpoint`: The streaming endpoint to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/connect(endpoint:))*