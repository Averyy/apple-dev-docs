# GKVoiceChatServiceError.Code

**Framework**: GameKit  
**Kind**: enum

Error codes for the voice chat service error domain.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum Code
```

## Topics

### Constants
- [GKVoiceChatServiceError.Code.internalError](gkvoicechatserviceerror-swift.struct/code/internalerror.md)
  A serious error occurred inside the voice chat service.
- [GKVoiceChatServiceError.Code.noRemotePacketsError](gkvoicechatserviceerror-swift.struct/code/noremotepacketserror.md)
  The voice chat service stopped receiving packets from the remote participant.
- [GKVoiceChatServiceError.Code.unableToConnectError](gkvoicechatserviceerror-swift.struct/code/unabletoconnecterror.md)
  The voice chat service was unable to establish a connection with another user.
- [GKVoiceChatServiceError.Code.remoteParticipantHangupError](gkvoicechatserviceerror-swift.struct/code/remoteparticipanthanguperror.md)
  The remote participant in a voice chat stopped the chat.
- [GKVoiceChatServiceError.Code.invalidCallIDError](gkvoicechatserviceerror-swift.struct/code/invalidcalliderror.md)
  The voice chat service didn’t recognize the call identifier.
- [GKVoiceChatServiceError.Code.audioUnavailableError](gkvoicechatserviceerror-swift.struct/code/audiounavailableerror.md)
  The audio hardware is unavailable to the voice chat service.
- [GKVoiceChatServiceError.Code.uninitializedClientError](gkvoicechatserviceerror-swift.struct/code/uninitializedclienterror.md)
  The application did not set a client before calling voice chat service methods.
- [GKVoiceChatServiceError.Code.clientMissingRequiredMethodsError](gkvoicechatserviceerror-swift.struct/code/clientmissingrequiredmethodserror.md)
  The voice chat service did not find an expected method defined by the client.
- [GKVoiceChatServiceError.Code.remoteParticipantBusyError](gkvoicechatserviceerror-swift.struct/code/remoteparticipantbusyerror.md)
  The remote participant is already connected to a voice chat.
- [GKVoiceChatServiceError.Code.remoteParticipantCancelledError](gkvoicechatserviceerror-swift.struct/code/remoteparticipantcancellederror.md)
  A remote participant attempted to start a voice chat, then canceled.
- [GKVoiceChatServiceError.Code.remoteParticipantResponseInvalidError](gkvoicechatserviceerror-swift.struct/code/remoteparticipantresponseinvaliderror.md)
  Invalid data was received from a remote participant.
- [GKVoiceChatServiceError.Code.remoteParticipantDeclinedInviteError](gkvoicechatserviceerror-swift.struct/code/remoteparticipantdeclinedinviteerror.md)
  A remote participant declined an invitation.
- [GKVoiceChatServiceError.Code.methodCurrentlyInvalidError](gkvoicechatserviceerror-swift.struct/code/methodcurrentlyinvaliderror.md)
  A method on the voice chat service was called when it was not allowed to be called (for example, attempting to connect when the voice chat service was already connected).
- [GKVoiceChatServiceError.Code.networkConfigurationError](gkvoicechatserviceerror-swift.struct/code/networkconfigurationerror.md)
  The voice chat service had problems accessing the network.
- [GKVoiceChatServiceError.Code.unsupportedRemoteVersionError](gkvoicechatserviceerror-swift.struct/code/unsupportedremoteversionerror.md)
  The other participant is running a different version of the voice chat service.
- [GKVoiceChatServiceError.Code.outOfMemoryError](gkvoicechatserviceerror-swift.struct/code/outofmemoryerror.md)
  The voice chat service was unable to allocate memory required to operate.
- [GKVoiceChatServiceError.Code.invalidParameterError](gkvoicechatserviceerror-swift.struct/code/invalidparametererror.md)
  A parameter had an unrecognized value.
### Initializers
- [init?(rawValue: Int32)](gkvoicechatserviceerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [GKGameSessionError.Code](gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerConnectionState](gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [enum GKPeerPickerConnectionType](gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [GKSessionError.Code](gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](gksessionerror-swift.struct.md)
- [enum GKSessionMode](gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror-swift.struct/code)*