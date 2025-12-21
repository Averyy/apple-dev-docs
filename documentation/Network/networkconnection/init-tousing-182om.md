# init(to:using:)

**Framework**: Network  
**Kind**: init

Create a new connection to an endpoint, with protocol stack.

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
convenience init(to endpoint: NWEndpoint, @ProtocolStackBuilder<ApplicationProtocol> using builder: () -> ApplicationProtocol)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/init(to:using:)-182om)*