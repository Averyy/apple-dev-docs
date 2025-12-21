# MultiplexProtocol

**Framework**: Network  
**Kind**: protocol

Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects.

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
protocol MultiplexProtocol : NetworkProtocolOptions
```

#### Overview

Generally network protocols conforming to this type will not directly expose send or receive methods. Instead, they expose methods to open and listen for multiplexed Subconnections which can send and receive.

## Relationships

### Inherits From
- [NetworkProtocolOptions](networkprotocoloptions.md)
### Conforming Types
- [QUIC](quic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/multiplexprotocol)*