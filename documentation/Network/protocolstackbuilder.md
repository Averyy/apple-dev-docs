# ProtocolStackBuilder

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

A resultBuilder for specifying and configuring protocol stacks in a declarative way

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
@resultBuilder
struct ProtocolStackBuilder<ApplicationProtocol, each P> where ApplicationProtocol : NetworkProtocolOptions, repeat each P : NetworkProtocolOptions
```

## Topics

### Type Methods
- [static func buildBlock(ApplicationProtocol, repeat each P) -> (ApplicationProtocol, repeat each P)](./protocolstackbuilder/buildblock%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/protocolstackbuilder)*