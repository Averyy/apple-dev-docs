# FoveatedStreamingSession.Endpoint

**Framework**: Foveated Streaming  
**Kind**: struct  
**Role**: Structure

A streaming endpoint that a foveated streaming session can connect to.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
struct Endpoint
```

## Mentions

- [Streaming a CloudXR application to Apple Vision Pro with foveation](../streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.md)

#### Overview

Use this object to specify the local or cloud streaming endpoint your foveated streaming session connects to when you call [`connect(endpoint:)`](./connect%28endpoint%29.md).

## Topics

### Type Properties
- [static var systemDiscovered: FoveatedStreamingSession.Endpoint](./endpoint/systemdiscovered.md)
  Connects to an endpoint the person selects from a list of endpoints the system discovers and presents.
### Type Methods
- [static func local(ipAddress: any IPAddress, port: NWEndpoint.Port) -> FoveatedStreamingSession.Endpoint](./endpoint/local%28ipaddress,port%29.md)
  Connects to a local endpoint by IP address and port number.
- [static func remote(serverName: String, signalingHeaders: [String : String]) -> FoveatedStreamingSession.Endpoint](./endpoint/remote%28servername,signalingheaders%29.md)
  Connects to a remote endpoint by server name.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/endpoint)*