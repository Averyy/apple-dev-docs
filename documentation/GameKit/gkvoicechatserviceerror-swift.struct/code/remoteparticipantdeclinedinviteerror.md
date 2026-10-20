# GKVoiceChatServiceError.Code.remoteParticipantDeclinedInviteError

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

A remote participant declined an invitation.

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
case remoteParticipantDeclinedInviteError
```

```c
GKVoiceChatServiceRemoteParticipantDeclinedInviteError
```

## See Also

### Constants
- [GKVoiceChatServiceError.Code.internalError](./internalerror.md)
  A serious error occurred inside the voice chat service.
- [GKVoiceChatServiceError.Code.noRemotePacketsError](./noremotepacketserror.md)
  The voice chat service stopped receiving packets from the remote participant.
- [GKVoiceChatServiceError.Code.unableToConnectError](./unabletoconnecterror.md)
  The voice chat service was unable to establish a connection with another user.
- [GKVoiceChatServiceError.Code.remoteParticipantHangupError](./remoteparticipanthanguperror.md)
  The remote participant in a voice chat stopped the chat.
- [GKVoiceChatServiceError.Code.invalidCallIDError](./invalidcalliderror.md)
  The voice chat service didn’t recognize the call identifier.
- [GKVoiceChatServiceError.Code.audioUnavailableError](./audiounavailableerror.md)
  The audio hardware is unavailable to the voice chat service.
- [GKVoiceChatServiceError.Code.uninitializedClientError](./uninitializedclienterror.md)
  The application did not set a client before calling voice chat service methods.
- [GKVoiceChatServiceError.Code.clientMissingRequiredMethodsError](./clientmissingrequiredmethodserror.md)
  The voice chat service did not find an expected method defined by the client.
- [GKVoiceChatServiceError.Code.remoteParticipantBusyError](./remoteparticipantbusyerror.md)
  The remote participant is already connected to a voice chat.
- [GKVoiceChatServiceError.Code.remoteParticipantCancelledError](./remoteparticipantcancellederror.md)
  A remote participant attempted to start a voice chat, then canceled.
- [GKVoiceChatServiceError.Code.remoteParticipantResponseInvalidError](./remoteparticipantresponseinvaliderror.md)
  Invalid data was received from a remote participant.
- [GKVoiceChatServiceError.Code.methodCurrentlyInvalidError](./methodcurrentlyinvaliderror.md)
  A method on the voice chat service was called when it was not allowed to be called (for example, attempting to connect when the voice chat service was already connected).
- [GKVoiceChatServiceError.Code.networkConfigurationError](./networkconfigurationerror.md)
  The voice chat service had problems accessing the network.
- [GKVoiceChatServiceError.Code.unsupportedRemoteVersionError](./unsupportedremoteversionerror.md)
  The other participant is running a different version of the voice chat service.
- [GKVoiceChatServiceError.Code.outOfMemoryError](./outofmemoryerror.md)
  The voice chat service was unable to allocate memory required to operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror-swift.struct/code/remoteparticipantdeclinedinviteerror)*