# FoveatedStreamingSession.DisconnectReason

**Framework**: Foveated Streaming  
**Kind**: struct

A description of why a foveated streaming session’s status is in the disconnected state.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
struct DisconnectReason
```

#### Overview

This struct may also be thrown as an error.

## Topics

### Type Properties
- [static var appInitiatedDisconnect: FoveatedStreamingSession.DisconnectReason](foveatedstreamingsession/disconnectreason/appinitiateddisconnect.md)
  A disconnect reason indicating the disconnect was initiated by the application.
- [static var endpointInitiatedDisconnect: FoveatedStreamingSession.DisconnectReason](foveatedstreamingsession/disconnectreason/endpointinitiateddisconnect.md)
  A disconnect command was initiated by the remote endpoint.
- [static var unauthorized: FoveatedStreamingSession.DisconnectReason](foveatedstreamingsession/disconnectreason/unauthorized.md)
  A disconnect reason indicating the person denied authorization of the foveated streaming session.
- [static var unavailable: FoveatedStreamingSession.DisconnectReason](foveatedstreamingsession/disconnectreason/unavailable.md)
  A disconnect reason indicating the foveated streaming service is currently unavailable.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/disconnectreason)*