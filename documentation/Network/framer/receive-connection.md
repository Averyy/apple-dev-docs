# receive(connection:)

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
static func receive<ConnectionType>(connection: ConnectionType) async throws -> Framer<T>.Message<Data> where ConnectionType : ConnectionProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/framer/receive(connection:))*