# send(connection:content:metadata:)

**Framework**: Network  
**Kind**: method

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
static func send<ConnectionType>(connection: ConnectionType, content: Data, metadata: Framer<T>.Metadata) async throws where ConnectionType : ConnectionProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/framer/send(connection:content:metadata:))*