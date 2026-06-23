# FoveatedStreamingProvider.Endpoint.remote(url:signalingHeaders:)

**Framework**: Foveated Streaming  
**Kind**: case

A remote (cloud) streaming endpoint.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
case remote(url: URL, signalingHeaders: [String : String])
```

## Parameters

- `url`: The URL of the remote streaming server.
- `signalingHeaders`: HTTP headers forwarded to the server for authentication and session management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/endpoint/remote(url:signalingheaders:))*