# GKVoiceChatServiceError.Code.remoteParticipantResponseInvalidError

**Framework**: GameKit  
**Kind**: case

Invalid data was received from a remote participant.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case remoteParticipantResponseInvalidError
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror-swift.struct/code/remoteparticipantresponseinvaliderror)*