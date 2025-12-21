# FramerProtocol

**Framework**: Network  
**Kind**: protocol

Framer protocols allow custom framing and serialization of messages on a connection.

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
protocol FramerProtocol
```

#### Overview

A Network Framer is an instance of a protocol in a connection’s protocol stack that parses and writes messages on top of a transport protocol, such as a TLS stream. A framer can add and parse headers or delimiters around application data to provide a message-oriented abstraction.

## Topics

### Type Properties
- [static var definition: NWProtocolFramer.Definition](framerprotocol/definition.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/framerprotocol)*