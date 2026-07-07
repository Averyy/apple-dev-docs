# DTLS.PeerAuthentication

**Framework**: Network  
**Kind**: enum

PeerAuthentication specifies how to authenticate the peer end of the connection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/dtls/peerauthentication)*