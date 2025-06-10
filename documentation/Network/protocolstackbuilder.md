# ProtocolStackBuilder

**Framework**: Network  
**Kind**: struct

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
@resultBuilder
struct ProtocolStackBuilder<ApplicationProtocol, each P> where ApplicationProtocol : NetworkProtocolOptions, repeat each P : NetworkProtocolOptions
```

## Topics

### Type Methods
- [static func buildBlock(ApplicationProtocol, repeat each P) -> (ApplicationProtocol, repeat each P)](protocolstackbuilder/buildblock(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/protocolstackbuilder)*