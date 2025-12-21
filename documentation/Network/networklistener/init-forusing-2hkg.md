# init(for:using:)

**Framework**: Network  
**Kind**: init

Create a listener that advertises a service with a protocol stack to use for listening.

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
convenience init(for provider: (any ListenerProvider)? = nil, @ProtocolStackBuilder<ApplicationProtocol> using builder: () -> ApplicationProtocol) throws
```

## Parameters

- `provider`: The listener provider to use for advertising the service.
- `builder`: The protocol stack to use for incoming connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/init(for:using:)-2hkg)*