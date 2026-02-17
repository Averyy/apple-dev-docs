# local(ipAddress:port:)

**Framework**: Foveated Streaming  
**Kind**: method

Connects to a local endpoint by IP address and port number.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
static func local(ipAddress: String, port: Int) -> FoveatedStreamingSession.Endpoint
```

#### Discussion

> **Note**: The port is independent from the one used for streaming content, which is determined by the streaming provider.

## Parameters

- `ipAddress`: The IP of the local endpoint.
- `port`: The port to connect to for the session management connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/endpoint/local(ipaddress:port:))*