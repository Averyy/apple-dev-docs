# TLS.PeerAuthentication

**Framework**: Network  
**Kind**: enum

PeerAuthentication specifies how to authenticate the peer end of the connection.

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
enum PeerAuthentication
```

#### Overview

For clients, the default is `none`. For servers, the default is `required`.

## Topics

### Enumeration Cases
- [TLS.PeerAuthentication.none](tls/peerauthentication/none.md)
  Do not authenticate the peer.
- [TLS.PeerAuthentication.optional](tls/peerauthentication/optional.md)
  Requests the peer certificate, but if none is provided, proceed with the connection.
- [TLS.PeerAuthentication.required](tls/peerauthentication/required.md)
  Always authenticate the peer.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls/peerauthentication)*