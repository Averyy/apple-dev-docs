# init(for:using:)

**Framework**: Network  
**Kind**: init

Create a listener that advertises a service with a protocol stack and parameters to use for listening.

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
convenience init(for provider: (any ListenerProvider)? = nil, using builder: NWParametersBuilder<ApplicationProtocol>) throws
```

## Parameters

- `provider`: The listener provider to use for advertising the service.
- `builder`: The builder to use for constructing the protocol stack and parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/init(for:using:)-2vh87)*