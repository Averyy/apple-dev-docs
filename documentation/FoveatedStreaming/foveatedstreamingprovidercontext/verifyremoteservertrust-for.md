# verifyRemoteServerTrust(for:)

**Framework**: Foveated Streaming  
**Kind**: method

Verifies the server certificate presented in a TLS authentication challenge.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func verifyRemoteServerTrust(for challenge: URLAuthenticationChallenge) async -> Bool
```

#### Return Value

`true` if the server is trusted; `false` otherwise.

#### Discussion

Streaming provider extensions are responsible for calling this method when handling authentication challenges from `URLSession` (or equivalent) for remote streaming endpoints, to validate the server’s certificate before completing the connection.

## Parameters

- `challenge`: The authentication challenge to verify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovidercontext/verifyremoteservertrust(for:))*