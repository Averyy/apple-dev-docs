# init(on:for:using:)

**Framework**: Network  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
convenience init(on port: NWEndpoint.Port, for provider: any ListenerProvider, @ProtocolStackBuilder<ApplicationProtocol> using builder: () -> ApplicationProtocol) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/init(on:for:using:)-8cbpt)*