# DTLS.PeerAuthentication

**Framework**: Network  
**Kind**: enum

PeerAuthentication specifies how to authenticate the peer end of the connection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum PeerAuthentication
```

#### Overview

For clients, the default is `none`. For servers, the default is `required`.

## Topics

### Enumeration Cases
- [DTLS.PeerAuthentication.none](dtls/peerauthentication/none.md)
  Do not authenticate the peer.
- [DTLS.PeerAuthentication.optional](dtls/peerauthentication/optional.md)
  Requests the peer certificate, but if none is provided, proceed with the connection.
- [DTLS.PeerAuthentication.required](dtls/peerauthentication/required.md)
  Always authenticate the peer.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/peerauthentication)*