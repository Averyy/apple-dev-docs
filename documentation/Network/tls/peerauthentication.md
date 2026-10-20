# TLS.PeerAuthentication

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [TLS.PeerAuthentication.none](./peerauthentication/none.md)
  Do not authenticate the peer.
- [TLS.PeerAuthentication.optional](./peerauthentication/optional.md)
  Requests the peer certificate, but if none is provided, proceed with the connection.
- [TLS.PeerAuthentication.required](./peerauthentication/required.md)
  Always authenticate the peer.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tls/peerauthentication)*