# FoveatedStreamingSession.Endpoint

**Framework**: Foveated Streaming  
**Kind**: struct

A streaming endpoint that a foveated streaming session can connect to.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
struct Endpoint
```

#### Overview

Use this object to specify the local or cloud streaming endpoint your foveated streaming session connects to when you call [`connect(endpoint:)`](foveatedstreamingsession/connect(endpoint:).md).

## Topics

### Type Properties
- [static var systemDiscovered: FoveatedStreamingSession.Endpoint](foveatedstreamingsession/endpoint/systemdiscovered.md)
  Connects to an endpoint the person selects from a list of endpoints the system discovers and presents.
### Type Methods
- [static func local(ipAddress: String, port: Int) -> FoveatedStreamingSession.Endpoint](foveatedstreamingsession/endpoint/local(ipaddress:port:).md)
  Connects to a local endpoint by IP address and port number.
- [static func remote(serverName: String) -> FoveatedStreamingSession.Endpoint](foveatedstreamingsession/endpoint/remote(servername:).md)
  Connects to a remote endpoint by server name.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/endpoint)*