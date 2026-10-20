# FoveatedStreamingProviderEndpoint.Remote

**Framework**: Foveated Streaming  
**Kind**: struct  
**Role**: Structure

Information needed to connect to a remote (cloud) streaming endpoint.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
struct Remote
```

## Topics

### Instance Properties
- [let signalingHeaders: [String : String]](./remote/signalingheaders.md)
  HTTP headers forwarded to the server for authentication and session management.
- [let url: URL](./remote/url.md)
  The URL of the remote streaming server.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingproviderendpoint/remote)*