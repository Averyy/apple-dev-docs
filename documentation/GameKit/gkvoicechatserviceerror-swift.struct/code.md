# GKVoiceChatServiceError.Code

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Error codes for the voice chat service error domain.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: No longer supported

## Declaration

```swift
enum Code
```

```c
enum GKVoiceChatServiceError : int;
```

## Topics

### Constants
- [GKVoiceChatServiceError.Code.internalError](./code/internalerror.md)
  A serious error occurred inside the voice chat service.
- [GKVoiceChatServiceError.Code.noRemotePacketsError](./code/noremotepacketserror.md)
  The voice chat service stopped receiving packets from the remote participant.
- [GKVoiceChatServiceError.Code.unableToConnectError](./code/unabletoconnecterror.md)
  The voice chat service was unable to establish a connection with another user.
- [GKVoiceChatServiceError.Code.remoteParticipantHangupError](./code/remoteparticipanthanguperror.md)
  The remote participant in a voice chat stopped the chat.
- [GKVoiceChatServiceError.Code.invalidCallIDError](./code/invalidcalliderror.md)
  The voice chat service didn’t recognize the call identifier.
- [GKVoiceChatServiceError.Code.audioUnavailableError](./code/audiounavailableerror.md)
  The audio hardware is unavailable to the voice chat service.
- [GKVoiceChatServiceError.Code.uninitializedClientError](./code/uninitializedclienterror.md)
  The application did not set a client before calling voice chat service methods.
- [GKVoiceChatServiceError.Code.clientMissingRequiredMethodsError](./code/clientmissingrequiredmethodserror.md)
  The voice chat service did not find an expected method defined by the client.
- [GKVoiceChatServiceError.Code.remoteParticipantBusyError](./code/remoteparticipantbusyerror.md)
  The remote participant is already connected to a voice chat.
- [GKVoiceChatServiceError.Code.remoteParticipantCancelledError](./code/remoteparticipantcancellederror.md)
  A remote participant attempted to start a voice chat, then canceled.
- [GKVoiceChatServiceError.Code.remoteParticipantResponseInvalidError](./code/remoteparticipantresponseinvaliderror.md)
  Invalid data was received from a remote participant.
- [GKVoiceChatServiceError.Code.remoteParticipantDeclinedInviteError](./code/remoteparticipantdeclinedinviteerror.md)
  A remote participant declined an invitation.
- [GKVoiceChatServiceError.Code.methodCurrentlyInvalidError](./code/methodcurrentlyinvaliderror.md)
  A method on the voice chat service was called when it was not allowed to be called (for example, attempting to connect when the voice chat service was already connected).
- [GKVoiceChatServiceError.Code.networkConfigurationError](./code/networkconfigurationerror.md)
  The voice chat service had problems accessing the network.
- [GKVoiceChatServiceError.Code.unsupportedRemoteVersionError](./code/unsupportedremoteversionerror.md)
  The other participant is running a different version of the voice chat service.
- [GKVoiceChatServiceError.Code.outOfMemoryError](./code/outofmemoryerror.md)
  The voice chat service was unable to allocate memory required to operate.
- [GKVoiceChatServiceError.Code.invalidParameterError](./code/invalidparametererror.md)
  A parameter had an unrecognized value.
### Initializers
- [init?(rawValue: Int32)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated enumerations
- [GKGameSessionError.Code](../gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerConnectionState](../gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [enum GKPeerPickerConnectionType](../gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](../gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [GKSessionError.Code](../gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](../gksessionerror-swift.struct.md)
- [enum GKSessionMode](../gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [struct GKVoiceChatServiceError](../gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror-swift.struct/code)*