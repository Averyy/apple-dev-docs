# withNetworkConnection(to:using:_:)

**Framework**: Network  
**Kind**: func

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func withNetworkConnection<ApplicationProtocol>(to endpoint: NWEndpoint, using builder: NWParametersBuilder<ApplicationProtocol>, _ handler: (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws where ApplicationProtocol : OneToOneProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-887ho)*